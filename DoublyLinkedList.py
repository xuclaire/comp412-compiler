class Node:
    def __init__(self):
        self.data = [-1] * 14
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.all_nodes = []
        self.nodes_list = []

    def __repr__(self):
        node = self.head
        while node is not None:
            self.all_nodes.append(node.data)
            node = node.next
        
        self.all_nodes.append("None")
        return "-> ".join(str(node) for node in self.all_nodes)

    def all_nodes_list(self):
        return self.nodes_list
    
    def add_node(self, node):
        node.next = self.head
        node.prev = None

        if self.head is not None:
            self.head.prev = node

        self.head = node
        self.nodes_list.append(node.data)
            