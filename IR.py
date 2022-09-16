from DoublyLinkedList import DoublyLinkedList
from collections import deque
import sys

class IR:
    def __init__(self):
        self.queue = []
        self.opcode_index = ("load", "store", "loadI", "add", "sub", "mult", "lshift", "rshift", "output", "nop")

    def add_list(self, new_list):
        self.queue.append(new_list)

    def print_me(self):
        print ("Print Format: [Opcode", "SR", "VR", "PR", "NU", "SR", "VR", "PR", "NU", \
            "SR", "VR", "PR", "NU", "LN PRINT]")
        while self.queue:
            dl_list = self.queue.pop(0)
            print dl_list.record
    