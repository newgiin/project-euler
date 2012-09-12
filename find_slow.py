#
# Find slow P.E. solutions I should speed up...
#
import euler
import signal

class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException()  

signal.signal(signal.SIGALRM, timeout_handler)

for i in range(1, 50):
    func_name = "euler.e_" + str(i) + "()"
    try:
        signal.alarm(5)
        print func_name + ": ",
        exec(func_name)
    except AttributeError:
    	print "Not implemented."
    except TimeoutException:
        print "This is taking too long!" 
    except IOError, e:
        print e # Missing file required for this problem
