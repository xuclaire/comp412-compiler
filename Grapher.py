import Renamer
from GraphEdge import GraphEdge
from GraphNode import GraphNode

class Grapher:
    def __init__(self, IR):
        self.IR = IR
        self.num_ops = len(self.IR)
        self.Map = {}
        self.node_map = {} #maps register number to node
        self.undef_node = GraphNode(None, None)
        self.node_num = 0
        self.edges = []
        self.prev_memops = []

        # type to latency
        self.type_latency = {"load": 5, "store": 5, "output": 1, "loadI": 1, "add": 1, "sub": 1, "mult": 3, "lshift": 1,
                     "rshift": 1, "nop": 1}
    
    def build_graph(self):
        for i in range(self.num_ops):
            node = self.IR[i]
            
            current_opcode = node[1]

            defs = [] # VRs
            uses = []
            if node[1] != "output" and node[1] != "nop":
                if node[1] != "store":
                    defs.append(node[11])
                if node[1] == "store":
                    uses.append(node[3])
                    uses.append(node[11])
                else:
                    if node[1] != "loadI":
                        uses.append(node[3])
                        if node[7] != -1:
                            uses.append(node[7])
            
            graph_node = GraphNode(self.node_num, current_opcode)
            graph_node.latency = self.type_latency[current_opcode]
            if node[1] == 'loadI':
                graph_node.op = str(node[1] + " " + str(node[2])+ " => r" + str(node[11]))
            elif node[1] == 'output':
                graph_node.op = str(node[1] + " " + str(node[2]))
            elif node[7] == -1:
                graph_node.op = str(node[1]) + " r" + str(node[3]) + " => r" + str(node[11])
            else:
                graph_node.op = str(node[1]) + " r" + str(node[3]) + ", r" + str(node[7]) + " => r" + str(node[11])
            self.Map[graph_node] = []

            for d in defs:  
                self.node_map[d] = graph_node 
            for u in uses:
                if u not in self.node_map:
                    self.node_map[u] = self.undef_node
                graph_edge = GraphEdge(self.node_map[u], "data", self.type_latency[current_opcode])
                self.Map[graph_node].append(graph_edge)
                self.edges.append((graph_node, self.node_map[u]))
            #memory ops
            #if op type is one of load, store output
            if current_opcode == 'load' or current_opcode == 'store' or current_opcode == 'output':
                for dest_op, dest_node in self.prev_memops:
                    if (dest_op == 'load' or dest_op == 'store' or dest_op == 'output') and current_opcode == 'store':
                        if (graph_node, dest_node) not in self.edges:
                            graph_edge = GraphEdge(dest_node, "serial", self.type_latency[current_opcode])
                            self.Map[graph_node].append(graph_edge)
                    elif dest_op == 'store' and (current_opcode == 'load' or current_opcode == 'output'):
                        if (graph_node, dest_node) not in self.edges:
                            graph_edge = GraphEdge(dest_node, "conflict", self.type_latency[current_opcode])  
                            self.Map[graph_node].append(graph_edge)
                    elif dest_op == 'output' and current_opcode == 'output':
                        if (graph_node, dest_node) not in self.edges:
                            graph_edge = GraphEdge(dest_node, "serial", self.type_latency[current_opcode])      
                            self.Map[graph_node].append(graph_edge)

                self.prev_memops.append((current_opcode, graph_node))                
            self.node_num += 1

        

