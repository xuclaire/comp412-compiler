from Grapher import Grapher
from GraphEdge import GraphEdge
from GraphNode import GraphNode

class Scheduler:
    def __init__(self, Map, edges):
        self.Map = Map
        self.edges = edges
        self.all_priorities = []
        self.priority_map = {}
        self.type_latency = {"load": 5, "store": 5, "output": 1, "loadI": 1, "add": 1, "sub": 1, "mult": 3, "lshift": 1,
                     "rshift": 1, "nop": 1}
        self.current_cycle = 1
        self.set_ready = False
        self.dest_nodes = []
        self.ready = []
        self.active = []
        self.final_schedule = []
    
    def compute_priorities(self):
        for e in self.edges:
            self.dest_nodes.append(e[0])
        root_node = (set(self.Map.keys()) - set(self.dest_nodes)).pop()
        for target_node in self.Map.keys():
            self.compute_max_priority(root_node, target_node)
                
    def compute_max_priority(self, root_node, target_node):
        queue = []
        queue.append(root_node)
        root_node.max_latency_path_value = root_node.latency
        while queue:
            m = queue.pop(0) 
            current_value = m.max_latency_path_value
            for neighbor in self.Map[m]:
                neighbor_node = neighbor.destination_node
                potential_latency = current_value + neighbor_node.latency
                if neighbor_node.max_latency_path_value == None or potential_latency > neighbor_node.max_latency_path_value:
                    neighbor_node.max_latency_path_value = potential_latency
                if neighbor_node != target_node:
                    queue.append(neighbor_node)
        self.priority_map[target_node] = target_node.max_latency_path_value
        target_node.priority = target_node.max_latency_path_value

    def is_ready(self, node, active):
        readiness = False
        for x in self.Map[node]:
            node_x = x.destination_node
            if x.edge_type == 'serial':
                if node_x in active:
                    readiness = True
            if node_x.off_active:
                readiness = True  
        return readiness
            
    def create_schedule(self):
        #add all nodes with no outgoing edges
        for k, v in self.Map.items():
            if v == []:
                self.ready.append(k)
        while (len(self.active) + len(self.ready) != 0):
            if self.ready == []:
                nop = GraphNode(len(self.final_schedule), 'nop')
                nop.op = 'nop'
                self.final_schedule.append(nop) 
            if len(self.ready) != 0:
                highest_priority = 0
                selected_node = None
                for n in self.ready:
                    if n.priority > highest_priority:
                        highest_priority = n.priority
                        selected_node = n
                self.ready.remove(selected_node)
                self.active.append(selected_node)
                selected_node.issue_cycle = self.current_cycle
                self.final_schedule.append(selected_node)
            self.current_cycle += 1
            #copy active?
            active_copy = self.active
            for o in active_copy:
                if self.current_cycle == o.issue_cycle + o.latency:     
                    # remove o from Active
                    self.active.remove(o)
                    o.off_active = True
                    # for each op d that depends on o
                    #if op doesnt have edges then dont do anything
                    for d in self.Map[o]:
                        #for dependencies: serial IS in active, others NOT in active (off active)! = ready
                        if self.is_ready(d.destination_node, self.active) == True:
                            self.ready.append(d.destination_node)
            # for each multi-cycle operation o in Active                   
                # check ops that depend on o for early releases
                # add any early releases to Ready
        for i in self.final_schedule:
            print(i.op)
        # if len(self.final_schedule) % 2 != 0:
        #     nop = GraphNode(len(self.final_schedule), 'nop')
        #     nop.op = 'nop'
        #     self.final_schedule.append(nop)
        # it = iter(self.final_schedule)
        # for n in it:
        #     print('[' + str(n.op) + '; ' + str(next(it).op) + ']')
            



