import sys
import Constants

class Scanner:
    def __init__(self, file):
        self.line_number = 0
        self.file = open(sys.argv[2], 'r') 
        self.current_line = ""
        self.next_char_pointer = 0 
        self.char = ' '
        self.tokens = [] 
        self.total_file_tokens = [] 
        self.eol = False  
        self.eof = False
        self.scanner_errors = 0
        self.line_errors = 0

    def scan(self):
        lines = self.file.readlines()
        for i in lines:
            self.current_line = lines[lines.index(i)].lstrip()
            self.tokens = []
            self.line_number += 1
            #my_scanner = Scanner.Scanner(args)
            self.tokens = self.scan_line()
            for token in self.tokens:
                category = token[0]
                lexeme = token[1]
                constant_cat = Constants.categories[category]
                if category == Constants.CAT_CONSTANT or category == Constants.CAT_REGISTER:
                    constant_word = str(lexeme)
                else:
                    constant_word = Constants.words[lexeme]       
                print(str(self.line_number) + ": < " + constant_cat + ", " + constant_word + " >")
                self.total_file_tokens.append(token)  
        self.line_number += 1
        print(str(self.line_number) + ": < ENDFILE, \"\" >")
        self.total_file_tokens.append((Constants.CAT_EOF, Constants.WORDS_EOF))
        self.eof = True
        return self.total_file_tokens
    
    def scan_nextword(self):
        if self.char.isdigit():
            constant = "\""
            if self.char < '0' or self.char > '9':
                print("ERROR")
            n = 0
            while (self.char >= '0' and self.char <= '9'):
                constant += self.char
                t = int(self.char)
                self.next_char_pointer += 1
                if self.next_char_pointer == len(self.current_line):
                    self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
                    self.char = '\n'
                    eol = True
                else:
                    self.char = self.current_line[self.next_char_pointer]
                    n = n*10 + t
            constant += "\""
            while (self.char == ' ' or self.char == '\t'):    
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
            self.tokens.append((Constants.CAT_CONSTANT, constant))
        elif self.char == 's':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == 't':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 'o':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == 'r':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                        if self.char == 'e':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer]
                            if self.char == ' ' or self.char == '\t':
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = self.current_line[self.next_char_pointer] 
                            self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_STORE))
            elif self.char == 'u':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]  
                if self.char == 'b':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == ' ' or self.char == '\t':
                        while self.char == ' ' or self.char == '\t':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer]
                    self.tokens.append((Constants.CAT_ARITHOP, Constants.WORDS_SUB))
        elif self.char == 'l':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == 'o':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 'a':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == 'd':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                        if self.char == 'I':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer]
                            if self.char == ' ' or self.char == '\t':
                                while (self.char == ' ' or self.char == '\t'):
                                    self.next_char_pointer += 1
                                    self.char = self.current_line[self.next_char_pointer]   
                                self.tokens.append((Constants.CAT_LOADI, Constants.WORDS_LOADI))
                        elif self.char == ' ' or self.char == '\t':
                            while self.char == ' ' or self.char == '\t':
                                self.next_char_pointer += 1
                                self.char = self.current_line[self.next_char_pointer]
                            self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_LOAD))
            if self.char == 's':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 'h':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == 'i':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer] 
                        if self.char == 'f':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer] 
                            if self.char == 't':
                                self.next_char_pointer += 1
                                self.char = self.current_line[self.next_char_pointer]
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = self.current_line[self.next_char_pointer]
                                self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_LSHIFT))
        elif self.char == 'r':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer] 
            register = "\"r"               
            #add in actual register number
            if self.char == 's':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer] 
                if self.char == 'h':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer] 
                    if self.char == 'i':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer] 
                        if self.char == 'f':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer] 
                            if self.char == 't':
                                self.next_char_pointer += 1
                                self.char = self.current_line[self.next_char_pointer] 
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = self.current_line[self.next_char_pointer]
                                self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_RSHIFT))
            if self.char.isdigit():  
                register = "\"r"  
                if self.char < '0' or self.char > '9':
                    print("ERROR")
                n = 0
                while (self.char >= '0' and self.char <= '9'):
                    register += self.char
                    t = int(self.char)
                    self.next_char_pointer += 1
                    if self.next_char_pointer == len(self.current_line):
                        self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
                        self.char = '\n'
                        eol = True
                    else:
                        self.char = self.current_line[self.next_char_pointer]
                        n = n*10 + t
                register += "\""
                if self.char == ' ' or self.char == '\t':
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                self.tokens.append((Constants.CAT_REGISTER, register)) 
        elif self.char == 'm':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == 'u':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 'l':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == 't':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                        while self.char == ' ' or self.char == '\t':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer]
                        self.tokens.append((Constants.CAT_ARITHOP, Constants.WORDS_MULT))
        elif self.char == 'a':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == 'd':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 'd':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == ' ' or self.char == '\t':
                        while self.char == ' ' or self.char == '\t':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer]
                    self.tokens.append((Constants.CAT_ARITHOP, Constants.WORDS_ADD))
        elif self.char == 'n':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == 'o':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 'p':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                    self.tokens.append((Constants.CAT_NOP, Constants.WORDS_NOP))
        elif self.char == 'o':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == 'u':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == 't':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
                    if self.char == 'p':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                        if self.char == 'u':
                            self.next_char_pointer += 1
                            self.char = self.current_line[self.next_char_pointer]
                            if self.char == 't':
                                self.next_char_pointer += 1
                                self.char = self.current_line[self.next_char_pointer]
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = self.current_line[self.next_char_pointer]
                                self.tokens.append((Constants.CAT_OUTPUT, Constants.WORDS_OUTPUT))
        elif self.char == '=':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == '>':
                self.next_char_pointer += 1
                self.char = self.current_line[self.next_char_pointer]
                if self.char == ' ' or self.char == '\t':
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = self.current_line[self.next_char_pointer]
                self.tokens.append((Constants.CAT_INTO, Constants.WORDS_INTO))
        elif self.char == ',':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == ' ' or self.char == '\t':
                while self.char == ' ' or self.char == '\t':
                    self.next_char_pointer += 1
                    self.char = self.current_line[self.next_char_pointer]
            self.tokens.append((Constants.CAT_COMMA, Constants.WORDS_COMMA))
        elif self.char == '/':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == '/':
                self.next_char_pointer += len(self.current_line) - 2
                #print(self.next_char_pointer)
                self.char = '\n'
                #self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
                eol = True
            else:
                print("ERROR "+ str(self.line_number) + ': / is not a valid word.')
        elif self.char == '\r':
            self.next_char_pointer += 1
            self.char = self.current_line[self.next_char_pointer]
            if self.char == '\n':
                #self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
                self.next_char_pointer += 1
                self.eol = True
        elif self.char == '\n':
            #append EOL token
            #self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
            self.next_char_pointer += 1
            self.eol = True
        # elif self.char == None:
        #     print('gets here')
        #     self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
        #     self.eol = True
        else:
            self.scanner_errors += 1
            self.line_errors += 1
            print("ERROR " + str(self.line_number) + ": " + str(self.char) + " is not a valid token.")
            line_left = self.next_char_pointer + 1
            self.next_char_pointer += len(self.current_line) - line_left
            self.char = self.current_line[self.next_char_pointer]

    def scan_line(self):
        self.next_char_pointer = 0 
        if len(self.current_line) != 0:
            self.char = self.current_line[self.next_char_pointer]
        while self.next_char_pointer < len(self.current_line)-1 or self.eol == False:
            self.scan_nextword()
        if self.eol == True:
            self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
        return self.tokens
            