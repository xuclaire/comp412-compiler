import sys
import Constants

class Scanner:
    def __init__(self, file):
        self.line_number = 0
        self.next_char_pointer = 0 
        self.char = ' '
        self.tokens = []  
        self.eol = False  
        
    #TODO: change all the constants!! 
    #TODO: is this way of keeping track of the next char and pointer correct?
    
    def scan_nextword(self, current_line, line_number):
        if self.char.isdigit():
            if self.char < '0' or self.char > '9':
                print("ERROR")
            n = 0
            while (self.char >= '0' and self.char <= '9'):
                t = int(self.char)
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                n = n*10 + t
            while (self.char == ' ' or self.char == '\t'):    
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
            self.tokens.append((Constants.CAT_CONSTANT, Constants.CAT_CONSTANT))
        elif self.char == 's':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == 't':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 'o':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    if self.char == 'r':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                        if self.char == 'e':
                            self.next_char_pointer += 1
                            self.char = current_line[self.next_char_pointer]
                            if self.char == ' ' or self.char == '\t':
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = current_line[self.next_char_pointer] 
                                self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_STORE))
            elif self.char == 'u':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]  
                if self.char == 'b':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    while (self.char == ' ' or self.char == '\t'):
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                    self.tokens.append((Constants.CAT_ARITHOP, Constants.WORDS_SUB))
        elif self.char == 'l':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == 'o':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 'a':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    if self.char == 'd':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                        if self.char == 'I':
                            self.next_char_pointer += 1
                            self.char = current_line[self.next_char_pointer]
                            if self.char == ' ' or self.char == '\t':
                                while (self.char == ' ' or self.char == '\t'):
                                    self.next_char_pointer += 1
                                    self.char = current_line[self.next_char_pointer]   
                                self.tokens.append((Constants.CAT_LOADI, Constants.WORDS_LOADI))
                        elif self.char == ' ' or self.char == '\t':
                            while self.char == ' ' or self.char == '\t':
                                self.next_char_pointer += 1
                                self.char = current_line[self.next_char_pointer]
                            self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_LOAD))
            if self.char == 's':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 'h':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    if self.char == 'i':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer] 
                        if self.char == 'f':
                            self.next_char_pointer += 1
                            self.char = current_line[self.next_char_pointer] 
                            if self.char == 't':
                                self.next_char_pointer += 1
                                self.char = current_line[self.next_char_pointer]
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = current_line[self.next_char_pointer]
                                self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_LSHIFT))
        elif self.char == 'r':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]                
            #add in actual register number
            if self.char == 's':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer] 
                if self.char == 'h':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer] 
                    if self.char == 'i':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer] 
                        if self.char == 'f':
                            self.next_char_pointer += 1
                            self.char = current_line[self.next_char_pointer] 
                            if self.char == 't':
                                self.next_char_pointer += 1
                                self.char = current_line[self.next_char_pointer] 
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = current_line[self.next_char_pointer]
                                self.tokens.append((Constants.CAT_MEMOP, Constants.WORDS_RSHIFT))
            if self.char.isdigit():    
                if self.char < '0' or self.char > '9':
                    print("ERROR")
                n = 0
                while (self.char >= '0' and self.char <= '9'):  
                    t = int(self.char)
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    n = n*10 + t
                if self.char == ' ' or self.char == '\t':
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                self.tokens.append((Constants.CAT_REGISTER, Constants.CAT_CONSTANT)) 
        elif self.char == 'm':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == 'u':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 'l':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    if self.char == 't':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                        while self.char == ' ' or self.char == '\t':
                            self.next_char_pointer += 1
                            self.char = current_line[self.next_char_pointer]
                        self.tokens.append((Constants.CAT_ARITHOP, Constants.WORDS_MULT))
        elif self.char == 'a':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == 'd':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 'd':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                    self.tokens.append((Constants.CAT_ARITHOP, Constants.WORDS_ADD))
        elif self.char == 'n':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == 'o':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 'p':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                    self.tokens.append((Constants.CAT_NOP, Constants.WORDS_NOP))
        elif self.char == 'o':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == 'u':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == 't':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
                    if self.char == 'p':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                        if self.char == 'u':
                            self.next_char_pointer += 1
                            self.char = current_line[self.next_char_pointer]
                            if self.char == 't':
                                self.next_char_pointer += 1
                                self.char = current_line[self.next_char_pointer]
                                while self.char == ' ' or self.char == '\t':
                                    self.next_char_pointer += 1
                                    self.char = current_line[self.next_char_pointer]
                                self.tokens.append((Constants.CAT_OUTPUT, Constants.WORDS_OUTPUT))
        elif self.char == '=':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == '>':
                self.next_char_pointer += 1
                self.char = current_line[self.next_char_pointer]
                if self.char == ' ' or self.char == '\t':
                    while self.char == ' ' or self.char == '\t':
                        self.next_char_pointer += 1
                        self.char = current_line[self.next_char_pointer]
                self.tokens.append((Constants.CAT_INTO, Constants.WORDS_INTO))
        elif self.char == ',':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == ' ' or self.char == '\t':
                while self.char == ' ' or self.char == '\t':
                    self.next_char_pointer += 1
                    self.char = current_line[self.next_char_pointer]
            self.tokens.append((Constants.CAT_COMMA, Constants.WORDS_COMMA))
        elif self.char == '/':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == '/':
                self.comment = True
                self.next_char_pointer += len(current_line) - 2
                self.char = '\n'
        elif self.char == '\r':
            self.next_char_pointer += 1
            self.char = current_line[self.next_char_pointer]
            if self.char == '\n':
                self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
                self.next_char_pointer += 1
                self.eol = True
        elif self.char == '\n':
            #append EOL token
            self.tokens.append((Constants.CAT_NEWLINE, Constants.WORDS_NEWLINE))
            self.next_char_pointer += 1
            self.eol = True
        elif self.char == "":
            self.tokens.append((Constants.CAT_EOF, Constants.WORDS_EOF))
        else:
            print("ERROR " + str(line_number) + ": " + str(self.char) + " is not a valid token.")
            line_left = self.next_char_pointer + 1
            self.next_char_pointer += len(current_line) - line_left
            self.char = current_line[self.next_char_pointer]

    def scan_line(self, current_line, line_number):
        self.next_char_pointer = 0
        if len(current_line) == 0:
            self.tokens.append((Constants.CAT_EOF, Constants.WORDS_EOF))
            return self.tokens
        self.char = current_line[self.next_char_pointer]
        while self.next_char_pointer < len(current_line)-1 or self.eol == False:
            self.scan_nextword(current_line, line_number)
        return self.tokens