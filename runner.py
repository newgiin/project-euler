#!/usr/bin/python
import importlib
import euler
import argparse
import signal
import sys
import time

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()  

def run_sol(n, timeout=None, disp_time=False):
    print 'Euler #' + str(n) + ': ',
    try:
        sol = importlib.import_module('probs.e_' + str(n))
        if timeout is not None:
            signal.signal(signal.SIGALRM, timeout_handler)
            signal.alarm(timeout)
        start = time.time()
        sol.main()
        if disp_time:
            print '\tTIME: ' + str(time.time() - start) + 's'
    except ImportError:
    	print 'Not implemented.'
    except TimeoutException:
        print 'This is taking too long!' 
    except IOError, e:
        print e # Required file is missing
        
def main():
    parser = argparse.ArgumentParser(description='Runner for Project Euler solutions.')
    parser.add_argument('-t', dest='timeout', type=int, help='Set the maximum \
        time in seconds a problem is allowed to take.')
    parser.add_argument('-v', action='store_true', dest='disp_time', \
        help='Display time taken')
    parser.add_argument('probs', metavar='P', nargs='*', help='Problem to solve')
    args = parser.parse_args()
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)        
        
    for p in args.probs:
        xs = p.split('-')
        if len(xs) == 2:
            for i in range(int(xs[0]), int(xs[1])+1, args.disp_time):
                run_sol(i, args.timeout, args.disp_time)
        else:
            run_sol(int(xs[0]), args.timeout, args.disp_time)
        
        
if __name__ == '__main__':
    main()        
