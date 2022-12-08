class GraphNode:
    def __init__(self, op_number, op_code):
        self.op_number = op_number
        self.op_code = op_code
        self.op = ""
        self.latency = 0
        self.max_latency_path_value = None #heaviest latency up to that node
        self.priority = 0
        self.issue_cycle = 0
        self.off_active = False
        self.is_ready = False
        self.delay = None

