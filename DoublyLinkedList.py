class DoublyLinkedList:
    def __init__(self):
        self.record = [None for i in range(15)]
        self.record[14] = True

    def write(self, index, content):
        self.record[index] = content