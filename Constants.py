categories = ["MEMOP", "LOADI", "ARITHOP", "OUTPUT", "NOP", "CONST", "REG", "COMMA", "INTO", "ENDFILE", "EOL", "NEWLINE"]
words = ['"load"', '"store"', '"loadl"', '"add"', '"sub"', '"mult"', '"lshift"', '"rshift"', '"output"', '"nop"', '","', '"=>"', '"\\n"', '"EOL"', '"constant"', '"register"', '""']

CAT_MEMOP = 0
CAT_LOADI = 1
CAT_ARITHOP = 2
CAT_OUTPUT = 3
CAT_NOP = 4
CAT_CONSTANT = 5
CAT_REGISTER = 6
CAT_COMMA = 7
CAT_INTO = 8
CAT_EOF = 9
CAT_EOL = 10
CAT_NEWLINE = 11

WORDS_LOAD = 0
WORDS_STORE = 1
WORDS_LOADI = 2
WORDS_ADD = 3
WORDS_SUB = 4
WORDS_MULT = 5
WORDS_LSHIFT = 6
WORDS_RSHIFT = 7
WORDS_OUTPUT = 8
WORDS_NOP = 9
WORDS_COMMA = 10
WORDS_INTO = 11
WORDS_NEWLINE = 12
WORDS_EOL = 13
WORDS_CONSTANT = 14
WORDS_REGISTER = 15
WORDS_EOF = 16