def main():
    def is_pandigital(x):
        x = str(x)
        n = len(x)
        digits = []
        for i in xrange(1, n + 1):
            digits.append(str(i))
        for i in xrange(len(digits)):
            if digits[i] not in x:
                return False
        return True
    
    primes = e_util.find_primes(99999999)
    for i in reversed(primes):
        if is_pandigital(i):
            print i
            break
        
if __name__ == '__main__':
    main()
