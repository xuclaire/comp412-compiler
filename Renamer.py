import Parser
import sys

class Renamer:
    def __init__(self, max_sr):
        self.vr_name = -1
        self.parse = Parser.Parser()
        self.parse.parse()
        self.max_sr = max_sr
        self.IR = self.parse.nodes_list
        self.sr_to_vr = ["invalid" for i in range(int(self.max_sr) + 1)]
        self.lu = [float('inf') for i in range(int(self.max_sr) + 1)]
        self.final_list = []  

    def rename(self):
        index = len(self.IR)
        for index in range(index-1, -1, -1):
            node = self.IR[index]
            #define registers  
            # add in not store case    
            node[10] = int(node[10])    
            if node[1] == "store":
                if self.sr_to_vr[node[10]] == "invalid":
                    self.vr_name += 1
                    self.sr_to_vr[node[10]] = self.vr_name
                #node[2] = self.sr_to_vr[2]
                node[11] = self.sr_to_vr[node[10]]
                node[13] = self.lu[node[10]]
                self.lu[node[10]] = index

            if node[10] != -1 and node[1] != "store":         
                if self.sr_to_vr[node[10]] == "invalid":
                    self.vr_name += 1
                    self.sr_to_vr[node[10]] = self.vr_name
                #node[10] = self.sr_to_vr[10]
                node[11] = self.sr_to_vr[node[10]]
                node[13] = self.lu[node[10]]

                self.sr_to_vr[node[10]] = "invalid"
                self.lu[node[10]] = float('inf')

            #use registers
            node[2] = int(node[2])
            if node[2] != -1 and node[1] != 'loadI' and node[1] != 'output':
                if self.sr_to_vr[node[2]] == "invalid":
                    self.vr_name += 1
                    self.sr_to_vr[node[2]] = self.vr_name
                #node[2] = self.sr_to_vr[2]
                node[3] = self.sr_to_vr[node[2]]
                node[5] = self.lu[node[2]]
                self.lu[node[2]] = index
        

            node[6] = int(node[6])
            if node[6] != -1:
                if self.sr_to_vr[node[6]] == "invalid":
                    self.vr_name += 1
                    self.sr_to_vr[node[6]] = self.vr_name
                #node[6] = self.sr_to_vr[6]
                node[7] = self.sr_to_vr[node[6]]
                node[9] = self.lu[node[6]]
                self.lu[node[6]] = index
            
    def print_nodes(self):       
        #check for loadi and output case = dont add a register 
        for node in self.IR:
            if node[1] == 'loadI':
                print(str(node[1] + " " + str(node[2])+ " => r" + str(node[11])))
            elif node[1] == 'output':
                print(str(node[1] + " " + str(node[2])))
            elif node[7] == -1:
                print(str(node[1]) + " r" + str(node[3]) + " => r" + str(node[11]))
            else:
                print(str(node[1]) + " r" + str(node[3]) + ", r" + str(node[7]) + " => r" + str(node[11]))
