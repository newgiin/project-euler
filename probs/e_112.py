def is_bouncy(x):
    is_inc = is_dec = True
    x = str(x)
    for i in xrange(0, len(x) - 1):
        if x[i] < x[i + 1]:
            is_dec = False
        if x[i] > x[i + 1]:
            is_inc = False
        if not (is_inc or is_dec):
            return True
    return not (is_inc or is_dec)
        
def main():
    total_bouncy = 0
    i = 1
    digits2mem = 5 # Limits lookup table size. Best speedup at 5.
    max_lkup_size = 10**digits2mem
    mem = set()

    while i < max_lkup_size:
        i_str = str(i)
        # Bouncy numbers within a number means the whole number is bouncy
        if is_bouncy(i):
            total_bouncy += 1
            mem.add(str(i))
        if float(total_bouncy) / i == .99:
            print i
            return
        i += 1
    
    # Memoize numbers containing <= 'digits2mem' digits.
    while True:
        i_str = str(i)
        # Bouncy numbers within a number means the whole number is bouncy
        if i_str[len(i_str) - digits2mem : ] in mem or is_bouncy(i):
            total_bouncy += 1
        if float(total_bouncy) / i == .99:
            print i
            return
        i += 1
        
if __name__ == '__main__':
    main()
