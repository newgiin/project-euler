def main():
    def is_circular(n):
        n = list(str(n))
        for i in xrange(len(n) - 1):
            last = n[len(n) - 1]
            for c in xrange(len(n) - 2, -1, -1):
                n[c + 1] = n[c]
            n[0] = last
            if e_util.is_prime(int("".join(n))) == False:
                return False
        return True

    primes = e_util.get_primes(1000000)

    # count number of circular primes
    count = 0
    for i in xrange(len(primes)):
        if is_circular(primes[i]):
            count += 1
    print count
    
if __name__ == '__main__':
    main()
