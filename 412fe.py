import sys
import getopt
import Constants
import Scanner

#ADD THE PART WHERE YOU DEFAULT TO -P IF NO CMD LINE ARG

def usage():    
    print("\nThis is a list of valid command line arguments to use: \n")
    print('-h: Outputs a list of all valid command line arguments to use')
    print('-s <name>: Reads the file specified by <name> and outputs a list of the tokens that the scanner found.')
    print('-p <name>: Reads thes file specified by <name>, scans and parses it, builds the intermediate representation, and reports success or failure.')
    print('-r <name>: Reads thes file specified by <name>, scans and parses it, and builds and prints the intermediate representation.')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 's:p:r:h')
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
    if args:
        if len(args) == 1:
            #parse the args[0] (insert the parse function)
            return
        else:
            print ("args", args)
            usage()
            sys.exit()

    for opt, args in opts:
        opt = opt[:2]
        if opt == '-h':
            usage()
            sys.exit()
        elif opt == '-s':
            file = open(sys.argv[2], 'r') 
            lines = file.readlines()
            line_number = 0
            for i in lines:
                current_line = lines[lines.index(i)].lstrip()
                line_number += 1
                my_scanner = Scanner.Scanner(args)
                tokens = my_scanner.scan_line(current_line, line_number)
                for token in tokens:
                    category = token[0]
                    lexeme = token[1]
                    constant_cat = Constants.categories[category]
                    constant_word = Constants.words[lexeme]
                    print(str(line_number) + ": < " + constant_cat + ", " + constant_word + " >")      
        elif opt == '-p' or not opts:
            #parse the a
            print("parsing")
        elif opt == '-r':
            #run the a
            print("running")
        elif opt == '' or opt == ' ':
            opt = '-p'
            print("parsing")
        else:
            usage()
            sys.exit(2)


if __name__ == "__main__":
    main()