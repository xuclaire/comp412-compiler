class GraphEdge:
    def __init__(self, destination_node, edge_type, source_latency):
        self.destination_node = destination_node
        self.edge_type = edge_type #data or conflict? 
        self.source_latency = source_latency #latency of source node
        