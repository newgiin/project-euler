#!/usr/bin/python
import euler
import argparse
import signal
import sys

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()  

def run_sol(n, timeout):
    func_name = "euler.e_" + str(n) + "()"
    print "Euler #" + str(n) + ": ",
    
    if timeout is not None:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
    try:
        exec(func_name)
    except AttributeError:
    	print "Not implemented."
    except TimeoutException:
        print "This is taking too long!" 
    except IOError, e:
        print e # Required file is missing

def run_range(lwr, upr, timeout):
    for i in range(lwr, upr+1):
        run_sol(i, timeout)
        
def main():
    parser = argparse.ArgumentParser(description="Runner for Project Euler solutions.")
    parser.add_argument("-r", dest="range", metavar=("LWR", "UPR"), nargs=2, 
        type=int, help="Get solutions to problems between LWR and UPR, inclusive.")
    parser.add_argument("-t", dest="timeout", type=int, help="Set the maximum time in seconds\
        a problem is allowed to take.")
    parser.add_argument("probs", metavar="P", nargs="*", type=int, help="Problem to solve")
    args = parser.parse_args()
    
    if (len(sys.argv) == 1):
        parser.print_help()
        sys.exit(1)        
        
    if args.range is not None:
        run_range(args.range[0], args.range[1], args.timeout)
    for p in args.probs:
        run_sol(p, args.timeout)
        
        
if __name__ == "__main__":
    main()        
