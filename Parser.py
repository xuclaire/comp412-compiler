import sys
import Scanner
import Constants
import IR
import DoublyLinkedList

class Parser:
    #add in line number
    def __init__(self):
        self.file = open(sys.argv[2], 'r')
        self.scanner = Scanner.Scanner(self.file)
        self.next_token = ""
        self.all_words = self.scanner.scan()
        self.words_pointer = -1
        self.parser_errors = 0
        self.scanner_errors = self.scanner.scanner_errors
        self.num_error_lines = self.scanner.line_errors
        self.line_number =  self.scanner.line_number
        self.IR = IR.IR()
        self.new_record = DoublyLinkedList.DoublyLinkedList()
        self.result = False
    
    def print_IR(self):
        self.IR.print_me()
    
    def get_nextword(self):
        self.words_pointer += 1
        if self.words_pointer < len(self.all_words):
            return self.all_words[self.words_pointer] 

    def find_nextline(self):
        start = self.all_words[self.words_pointer]
        while(start == "NEWLINE"):
            self.words_pointer += 1
        return self.all_words[self.words_pointer]
            
    def parse(self):     
        category = ""
        while category != "ENDFILE":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            self.new_record = DoublyLinkedList.DoublyLinkedList()
            self.new_record.write(0, word[1])
            if category == "MEMOP":
                self.finish_memop()
            elif category == "LOADI":
                self.finish_loadI()
            elif category == "ARITHOP":
                self.finish_arithop()
            elif category == "OUTPUT":
                self.finish_output()
            elif category == "NOP":
                self.finish_nop()
            elif category == "NEWLINE":
                continue
            else:
                continue

    def finish_memop(self):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        if category == "REG":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "INTO":
                word = self.get_nextword()
                category = Constants.categories[word[0]]
                if category == "REG":
                    word = self.get_nextword()
                    category = Constants.categories[word[0]]
                    if category == "NEWLINE":
                        self.new_record.write(1, word[1])
                        self.result = True
                    else:
                        print("ERROR " + str(self.line_number) + ": Missing newline.")
                        self.parser_errors += 1
                        self.num_error_lines += 1
                else:
                    print("ERROR " + str(self.line_number) + ": Missing a target register.")
                    self.parser_errors += 1
                    self.num_error_lines += 1
            else:
                print("ERROR " + str(self.line_number) + ": Missing '=>'.")
                self.parser_errors += 1
                self.num_error_lines += 1
        else:
            print("ERROR " + str(self.line_number) + ": Missing a source register.")
            self.parser_errors += 1
            self.num_error_lines += 1

    def finish_loadI(self):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        if category == "CONST":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "INTO":
                word = self.get_nextword()
                category = Constants.categories[word[0]]
                if category == "REG":
                    word = self.get_nextword()
                    category = Constants.categories[word[0]]
                    if category == "NEWLINE":
                        self.new_record.write(9, word[1])
                        self.result = True
                        return 0
                    else:
                        print("ERROR " + str(self.line_number) + ": Missing newline.")
                        self.parser_errors += 1
                        self.num_error_lines += 1
                else:
                    self.parser_errors += 1
                    self.num_error_lines += 1
                    print("ERROR " + str(self.line_number) + ": Missing a target register.")
            else:
                self.parser_errors += 1
                self.num_error_lines += 1
                print("ERROR " + str(self.line_number) + ": Missing '=>'.")
        else:
            self.parser_errors += 1
            self.num_error_lines += 1
            print("ERROR " + str(self.line_number) + ": Missing constant.")

    def finish_arithop(self):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        if category == "REG":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "COMMA":
                word = self.get_nextword()
                category = Constants.categories[word[0]]
                if category == "REG":
                    word = self.get_nextword()
                    category = Constants.categories[word[0]]
                    if category == "INTO":
                        word = self.get_nextword()
                        category = Constants.categories[word[0]]
                        if category == "REG":
                            word = self.get_nextword()
                            category = Constants.categories[word[0]]
                            if category == "NEWLINE":
                                self.new_record.write(9, word[1])
                                self.result = True
                            else:
                                print("ERROR " + str(self.line_number) + ": Missing newline.")
                                self.parser_errors += 1
                                self.num_error_lines += 1
                        else:
                            self.parser_errors += 1
                            self.num_error_lines += 1
                            print("ERROR " + str(self.line_number) + ": Missing target register.")
                    else:
                        self.parser_errors += 1
                        self.num_error_lines += 1
                        print("ERROR " + str(self.line_number) + ": Missing '=>'.")
                else:
                    self.parser_errors += 1
                    self.num_error_lines += 1
                    print("ERROR " + str(self.line_number) + ": Missing one of the source registers.")    
            else:
                self.parser_errors += 1
                self.num_error_lines += 1
                print("ERROR " + str(self.line_number) + ": Missing comma.")
        else:
            self.parser_errors += 1
            self.num_error_lines += 1
            print("ERROR " + str(self.line_number) + ": Missing one of the source registers.")

    def finish_output(self):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        if category == "CONST":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "NEWLINE":
                self.new_record.write(1, word[1])
                self.result = True
            else:
                self.num_error_lines += 1
                self.parser_errors += 1
                print("ERROR " + str(self.line_number) + ": Missing newline.")
        else:
            self.num_error_lines += 1
            self.parser_errors += 1
            print("ERROR " + str(self.line_number) + ": Missing output constant.")
        

    def finish_nop(self):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        if category == "NEWLINE":
            self.result = True
        else:
            self.num_error_lines += 1
            self.parser_errors += 1
            print("ERROR " + str(self.line_number) + ": Missing newline.")
        
        
