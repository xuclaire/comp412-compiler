import sys
import Scanner
import Constants
from DoublyLinkedList import Node
import DoublyLinkedList

class Parser:
    #add in line number
    def __init__(self):
        self.file = open(sys.argv[1], 'r')
        self.file_length = len(self.file.readlines())
        self.scanner = Scanner.Scanner(self.file)
        self.next_token = ""
        self.all_words = self.scanner.scan()
        self.words_pointer = -1
        self.parser_errors = 0
        self.scanner_errors = self.scanner.scanner_errors
        self.num_error_lines = self.scanner.line_errors
        self.line_number =  self.scanner.line_number
        self.result = False
        self.IR = DoublyLinkedList.DoublyLinkedList()
        self.nodes_list = self.IR.all_nodes_list()
        self.max_sr = 0

    def get_nextword(self):
        self.words_pointer += 1
        if self.words_pointer < len(self.all_words):
            return self.all_words[self.words_pointer] 
            
    def parse(self):     
        category = ""
        self.valid_operation = 0
        while category != "ENDFILE":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "MEMOP":
                self.finish_memop(Constants.words[word[1]])
            elif category == "LOADI":
                self.finish_loadI(Constants.words[word[1]])
            elif category == "ARITHOP":
                self.finish_arithop(Constants.words[word[1]])
            elif category == "OUTPUT":
                self.finish_output()
            elif category == "NOP":
                self.finish_nop()
            elif category == "NEWLINE":
                continue
            else:
                continue
        
        return self.max_sr
            
    def finish_memop(self, opcode):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        memop_node = Node()
        memop_node.data[0] = word[2]
        memop_node.data[1] = opcode[1:len(opcode)-1]
        memop_node.data[2] = word[1][2:len(word[1])-1]
        self.update_max_sr(int(word[1][2:len(word[1])-1]))
        if category == "REG":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "INTO":
                word = self.get_nextword()
                category = Constants.categories[word[0]]
                memop_node.data[10] = word[1][2:len(word[1])-1]
                self.update_max_sr(int(word[1][2:len(word[1])-1]))
                if category == "REG":
                    word = self.get_nextword()
                    category = Constants.categories[word[0]]
                    self.IR.add_node(memop_node)
                    self.result = True
                    # else:
                    #     print("ERROR " + str(self.line_number) + ": Missing newline.")
                    #     self.parser_errors += 1
                    #     self.num_error_lines += 1
                else:
                    print("ERROR " + str(self.line_number) + ": Missing a target register.")
                    self.parser_errors += 1
                    self.num_error_lines += 1
            else:
                #print('here 2')
                #print("ERROR " + str(self.line_number) + ": Missing '=>'.")
                self.parser_errors += 1
                self.num_error_lines += 1
        else:
            print("ERROR " + str(self.line_number) + ": Missing a source register.")
            self.parser_errors += 1
            self.num_error_lines += 1

    def finish_loadI(self, opcode):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        loadi_node = Node()
        loadi_node.data[0] = word[2]
        loadi_node.data[1] = opcode[1:len(opcode)-1]
        loadi_node.data[2] = word[1][1:len(word[1])-1]
        self.update_max_sr(int(word[1][1:len(word[1])-1]))
        if category == "CONST":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "INTO":
                word = self.get_nextword()
                category = Constants.categories[word[0]]
                loadi_node.data[10] = word[1][2:len(word[1])-1]
                self.update_max_sr(int(word[1][2:len(word[1])-1]))
                if category == "REG":
                    word = self.get_nextword()
                    category = Constants.categories[word[0]]
                    if category == "NEWLINE":
                        self.IR.add_node(loadi_node)
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

    def finish_arithop(self, opcode):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        arithop_node = Node()
        arithop_node.data[0] = word[2]
        arithop_node.data[1] = opcode[1:len(opcode)-1]
        arithop_node.data[2] = word[1][2:len(word[1])-1]
        self.update_max_sr(int(word[1][2:len(word[1])-1]))
        if category == "REG":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            if category == "COMMA":
                word = self.get_nextword()
                category = Constants.categories[word[0]]
                arithop_node.data[6] = word[1][2:len(word[1])-1]
                self.update_max_sr(int(word[1][2:len(word[1])-1]))
                if category == "REG":
                    word = self.get_nextword()
                    category = Constants.categories[word[0]]
                    if category == "INTO":
                        word = self.get_nextword()
                        category = Constants.categories[word[0]]
                        arithop_node.data[10] = word[1][2:len(word[1])-1]
                        self.update_max_sr(int(word[1][2:len(word[1])-1]))
                        if category == "REG":
                            word = self.get_nextword()
                            category = Constants.categories[word[0]]
                            if category == "NEWLINE":
                                self.IR.add_node(arithop_node)
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
        output_node = Node()
        output_node.data[0] = word[2]
        output_node.data[1] = "output"
        output_node.data[2] = word[1][1:len(word[1])-1]
        self.update_max_sr(int(word[1][1:len(word[1])-1]))
        if category == "CONST":
            word = self.get_nextword()
            category = Constants.categories[word[0]]
            self.IR.add_node(output_node)
            self.result = True
        else:
            self.num_error_lines += 1
            self.parser_errors += 1
            print("ERROR " + str(self.line_number) + ": Missing output constant.")
        

    def finish_nop(self):
        word = self.get_nextword()
        category = Constants.categories[word[0]]
        #if category == "NEWLINE":
            # nop_node = Node()
            # nop_node.data[0] = word[2]
            # nop_node.data[1] = "NOP"
            # nop_node.data[2] = word[1][1:len(word[1])-1]
            # self.update_max_sr(int(word[1][1:len(word[1])-1]))
            # self.IR.add_node(nop_node)
        self.result = True
        # else:
        #             self.num_error_lines += 1
        #     self.parser_errors += 1
        #     print("ERROR " + str(self.line_number) + ": Missing newline.")
    
    def update_max_sr(self, candidate):
        self.max_sr = max(self.max_sr, candidate)


        
