import sys
import getopt
import Parser
import Renamer
import Grapher
import Scheduler

def usage():    
    print("\nThis is a list of valid command line arguments to use: \n")
    print('-h: Outputs a list of all valid command line arguments to use')

def main():
    if sys.argv[1:2][0] == '-h':
        usage()
        sys.exit()  
    else:
        graph()
        

def graph():
    parser = Parser.Parser()
    max_sr = parser.parse()
    renamer = Renamer.Renamer(max_sr)
    IR, vr_name = renamer.rename()
    grapher = Grapher.Grapher(IR)
    grapher.build_graph()   
    dependence_graph = grapher.Map  
    edges = grapher.edges  
    scheduler = Scheduler.Scheduler(dependence_graph, edges)
    scheduler.compute_priorities()
    scheduler.create_schedule()
      
if __name__ == "__main__":
    main()
