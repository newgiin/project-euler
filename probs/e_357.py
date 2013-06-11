def is_prime_generating(n, primes):
    fs = e_util.get_factors(n)
    if len(fs) % 2 != 0:
        # if it has an integer root, 
        # it can't be prime-generating (since 2*root is not prime)
        return False
    for i in range(len(fs)/2):
        if (fs[i] + fs[len(fs) - 1 - i]) not in primes:
            return False
    return True

def main():
    sum = 1 # since 1 is prime generating
    n = 100000000
    primes = e_util.find_primes_set(n + 2)
    for i in range(2, n + 2, 2):
        if (i + 1 in primes and
                i / 2 + 2 in primes and
                is_prime_generating(i, primes)):
            sum += i
    print sum

if __name__ == '__main__':
    main()
