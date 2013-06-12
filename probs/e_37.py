def main():
    primes = e_util.find_primes(900000)
    result = []
    for i in xrange(4, len(primes)):
        s = str(primes[i])
        # remove from right to left
        truncable = True
        while len(s) > 1:
            s = s[0 : len(s) - 1]
            if int(s) not in primes:
                truncable = False
                break
        if truncable:
            # from left to right
            s = str(primes[i])
            while len(s) > 1:
                s = s[1 : len(s)]
                if int(s) not in primes:
                    truncable = False
                    break
        if truncable:
            result.append(primes[i])
    print sum(result)
    
if __name__ == '__main__':
    main()
