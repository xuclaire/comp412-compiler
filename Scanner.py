import sys

class Scanner:
    def init(self, file):
        self.file = file
        self.next_line = ""
        self.line_number = 0
        self.next_char_pointer = -1
    
    def read_nextline(self):
        return 0

    def scan_nextword(self):
        return 0

    def scan(self):
        return 0

    def next_character(self):
        self.next_char_pointer += 1
        try:
            self.next_char = self.next_line[self.next_char_pointer]
        except:
            print("ERROR")
    
    def rollback_character(self):
        self.next_char_pointer -= 1