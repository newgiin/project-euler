def main():
    # TODO
    result = 0
    i = 1
    digits2mem = 6
    max_lkup_size = 10**digits2mem
    mem = set()
    
    # Memoize numbers containing <= 'digits2mem' digits.
    while i < max_lkup_size:
        i_str = str(i)
        if i_str[len(i_str) - digits2mem : ] in mem or is_bouncy(i):
            mem.add(str(i))
        else:
            result += 1
        i += 1
    
    while i < 10**8:
        i_str = str(i)
        # Bouncy numbers within a number means the whole number is bouncy
        if i_str[len(i_str) - digits2mem : ] not in mem and not is_bouncy(i):
            result += 1   
        i += 1
        
    print result

 
if __name__ == '__main__':
    main()
