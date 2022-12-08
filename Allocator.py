import sys
import Renamer
from DoublyLinkedList import Node
import DoublyLinkedList

class Allocator:
    def __init__(self, pr_num, IR, vr_name):
        self.IR = IR
        self.vr_name = vr_name
        self.max_vr_num = self.vr_name
        self.max_pr_num = pr_num - 1
        self.vr2pr = [-1 for i in range(self.max_vr_num + 1)]
        self.pr2vr = [-1 for j in range(self.max_pr_num)]
        self.pr_nu = [float('inf') for k in range(self.max_pr_num)]
        self.available_prs = []
        for pr in range(0, self.max_pr_num):
            self.available_prs.append(pr)
        self.inserted_lines = 0
        self.spill_locations = [-1 for a in range(self.max_vr_num + 1)]
        #self.loadI_vrs = ["invalid" for b in range(self.max_vr_num + 1)]
        #self.load_vrs = ["invalid" for c in range(self.max_vr_num + 1)]
        self.start_spill_location = 32768
        self.index = 0

    def allocate(self):
        for i in range(0, len(self.IR)):
            node = self.IR[i]
            marks = [0] * (self.max_pr_num + 1)
            defs = [] # indices of SRs
            uses = []
            if node[1] != "output" and node[1] != "nop":
                if node[1] != "store":
                    defs.append(10)
                if node[1] == "store":
                    uses.append(2)
                    uses.append(10)
                else:
                    if node[1] != "loadI":
                        uses.append(2)
                        if node[6] != -1:
                            #flag_2defs = True
                            uses.append(6)

            for u in uses:
                vr = u+1
                nu = u+3
                pr = self.vr2pr[node[vr]]
                if pr == -1:
                    node[u+2] = self.get_apr(self.index, node[vr], node[nu], marks)
                    if self.spill_locations[node[vr]] != -1:
                        self.restore(node[vr], node[u+2], self.index)
                else:
                    node[u+2] = pr
                marks[node[u+2]] = 1
                        
            for u in uses:
                vr = u+1
                pr = u+2
                nu = u+3
                if node[nu] == float('inf') and self.pr2vr[node[pr]] != -1:
                    self.free_apr(node[pr])
                else:
                    if node[pr] != -1:
                        self.pr_nu[node[pr]] = node[nu]
            
            marks = [0] * (self.max_pr_num + 1)

            for d in defs:
                vr = d+1
                pr = d+2
                nu = d+3
                node[pr] = self.get_apr(self.index, node[vr], node[nu], marks)
                marks[node[pr]] = 1

            for d in defs:
                vr = d+1
                pr = d+2
                nu = d+3
                if node[nu] == float('inf') and self.pr2vr[node[pr]] != -1:
                    self.free_apr(node[pr])
            
            if node[1] == 'loadI':
                #print(node)
                print(str(node[1] + " " + str(node[2])+ " => r" + str(node[12])))
            elif node[1] == 'output':
                print(str(node[1] + " " + str(node[2])))
            elif node[1] == 'load' or node[1] == 'store':
                print(str(node[1]) + " r" + str(node[4]) + " => r" + str(node[12]))
            else:
                print(str(node[1]) + " r" + str(node[4]) + ", r" + str(node[8]) + " => r" + str(node[12]))
            
           #self.print_lists()
            self.index += 1  

            
    def restore(self, vr, pr, spot):
        spot = spot + self.inserted_lines
        loadI_node = Node()
        loadI_node.data[0] = spot
        loadI_node.data[1] = "loadI"
        loadI_node.data[2] = self.spill_locations[vr]
        loadI_node.data[12] = self.max_pr_num
        print(str(loadI_node.data[1] + " " + str(loadI_node.data[2])+ " => r" + str(loadI_node.data[12])))
        #self.IR.insert(spot, loadI_node.data)
        self.inserted_lines += 1

        load_node = Node()
        load_node.data[0] = len(self.IR) + 1
        load_node.data[1] = "load"
        load_node.data[4] = self.max_pr_num 
        load_node.data[12] = pr
        print(str(load_node.data[1]) + " r" + str(load_node.data[4]) + " => r" + str(load_node.data[12]))
        #self.IR.insert(spot + 1, load_node.data)
        self.inserted_lines += 2
                
    def spill(self, pr, spot):
        spot = spot + self.inserted_lines
        loadI_node = Node()
        #loadI_node.data[0] = len(self.IR) + 1
        loadI_node.data[1] = "loadI"
        loadI_node.data[2] = self.start_spill_location 
        loadI_node.data[12] = self.max_pr_num
        print(str(loadI_node.data[1] + " " + str(loadI_node.data[2])+ " => r" + str(loadI_node.data[12])))
        #self.IR.insert(spot, loadI_node.data)

        store_node = Node()
        #store_node.data[0] = len(self.IR) + 1
        store_node.data[1] = "store"
        store_node.data[4] = pr
        store_node.data[12] = self.max_pr_num 
        print(str(store_node.data[1]) + " r" + str(store_node.data[4]) + " => r" + str(store_node.data[12]))
        #self.IR.insert(spot + 1, store_node.data)
        self.inserted_lines += 2

        self.spill_locations[self.pr2vr[pr]] = self.start_spill_location
        self.start_spill_location += 4
        self.vr2pr[self.pr2vr[pr]] = -1

    def free_apr(self, pr):
        self.vr2pr[self.pr2vr[pr]] = -1
        self.pr2vr[pr] = -1
        self.pr_nu[pr] = float('inf')
        self.available_prs.append(pr)

    def get_apr(self, spot, vr, nu, marks):
        x = -1
        if len(self.available_prs) != 0:
            x = self.available_prs.pop()
        else:
            #pick unmarked x
            #make this more efficient
            max_next_use = -1
            selected_pr = -1
            for pr, nu in enumerate(self.pr_nu):
                if (nu > max_next_use and marks[pr] == 0):
                    max_next_use  =  nu
                    selected_pr = pr 
            # for pr, mark in enumerate(marks):
            #     #print(self.pr_nu[pr])
            #     if mark == 0 and self.pr_nu[pr] > max_next_use:
            #         #print('finds unmarked')
            #         max_next_use  = self.pr_nu[pr]
            #         selected_pr =  pr
            #print("selected pr is " + str(selected_pr))
            x = selected_pr
            self.spill(int(x), spot)
        
        self.vr2pr[vr] = x
        self.pr2vr[x] = vr
        self.pr_nu[x] = nu
        return int(x)
        
    def print_lists(self):
        print("vr2pr" + str(self.vr2pr))
        print("pr2vr" + str(self.pr2vr))
        print("spill" + str(self.spill_locations))

    def print_nodes(self):
        for node in self.IR:
            if node[1] == 'loadI':
                print(str(node[1] + " " + str(node[2])+ " => r" + str(node[12])))
            elif node[1] == 'output':
                print(str(node[1] + " " + str(node[2])))
            elif node[1] == 'load' or node[1] == 'store':
                print(str(node[1]) + " r" + str(node[4]) + " => r" + str(node[12]))
            else:
                print(str(node[1]) + " r" + str(node[4]) + ", r" + str(node[8]) + " => r" + str(node[12]))

