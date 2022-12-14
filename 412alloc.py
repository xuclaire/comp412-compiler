import sys
import getopt
import Parser
import Renamer
import Allocator

def usage():    
    print("\nThis is a list of valid command line arguments to use: \n")
    print('-h: Outputs a list of all valid command line arguments to use')
    print('-x: Output for Lab 2 Code Check 1')

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'x:h')
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)    
    # if args:
    #     if len(args) == 1:
    #         return
    #     else:
    #         print ("args", args)
    #         usage()
    #         sys.exit() 
    if sys.argv[1].isdigit():
        if int(sys.argv[1]) > 64 or int(sys.argv[1]) < 3:
            print("ERROR!")
        else:
            allocate(int(sys.argv[1]))
    else:
        for opt, args in opts:
            opt = opt[:2]
            if opt == '-h':
                usage()
                sys.exit()  
            elif opt == '-x':
                parser = Parser.Parser()
                max_sr = parser.parse()
                renamer = Renamer.Renamer(max_sr)
                renamer.rename()
                renamer.print_nodes()

def allocate(k):
    parser = Parser.Parser()
    max_sr = parser.parse()
    renamer = Renamer.Renamer(max_sr)
    #vr_name = renamer.return_vr_name()
    #IR = renamer.return_IR()
    IR, vr_name = renamer.rename()
    #renamer.print_nodes()
    allocator = Allocator.Allocator(k, IR, vr_name)
    allocator.allocate()
    #allocator.print_nodes()
    
        
if __name__ == "__main__":
    main()