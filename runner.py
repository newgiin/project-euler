#!/usr/bin/python
import importlib
import euler
import argparse
import signal
import sys

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()  

def run_sol(n, timeout, disp_time=False):
    print "Euler #" + str(n) + ": ",
    try:
        sol = importlib.import_module('probs.e_' + str(n))
        if timeout is not None:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)
        sol.main()
    except ImportError:
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
    parser.add_argument("-t", dest="timeout", type=int, help="Set the maximum \
        time in seconds a problem is allowed to take.")
    parser.add_argument("-v", dest="disp_time", type=bool, help="Display time taken")
    parser.add_argument("probs", metavar="P", nargs="*", help="Problem to solve")
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)        
        
    for p in args.probs:
        xs = p.split('-')
        if len(xs) == 2:
            run_range(int(xs[0]), int(xs[1]), args.timeout)
        else:
            run_sol(int(xs[0]), args.timeout)
        
        
if __name__ == "__main__":
    main()        
