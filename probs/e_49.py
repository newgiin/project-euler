def main():
    primes = e_util.find_primes(10000)
    for i in xrange(0, len(primes) - 3):
        for j in xrange(i + 1, len(primes) - 2): 
            if e_util.is_perm(str(primes[i]), str(primes[j])):
                diff = primes[j] - primes[i]
                try:
                    partner = primes.index(primes[j] + diff)
                except ValueError:
                    partner = -1
                if partner != -1 and e_util.is_perm(str(primes[j]), str(primes[partner])):
                    print primes[i], primes[j], primes[partner]

if __name__ == '__main__':
    main()
