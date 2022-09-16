import sys
import getopt
import Constants
import Scanner
import Parser

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
            scanner = Scanner.Scanner(args)
            scanner.scan()
        elif opt == '-p' or not opts:
            #parse the a
            parser = Parser.Parser()
            parser.parse()
            parser_errors = parser.parser_errors
            scanner_errors = parser.scanner_errors
            line_errors = parser.num_error_lines
            if parser_errors > 0 or scanner_errors > 0 or line_errors > 0:
                print("Found " + str(scanner_errors + parser_errors) + " errors on " + str(line_errors) + " lines.")
            else:
                print("Parse successful, no errors!")

        elif opt == '-r':
            #run the a
            parser = Parser.Parser()
            parser.parse()
            errors = parser.parser_errors
            if errors > 0:
                print("Due to syntax errors, run terminates.")
            else:
                print("Run successful!")
        elif opt == '' or opt == ' ':
            opt = '-p'
        else:
            usage()
            sys.exit(2)

if __name__ == "__main__":
    main()