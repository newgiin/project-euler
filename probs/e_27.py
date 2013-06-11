def main():
    max_primes = 0
    max_a = 0
    max_b = 0
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            n = 0
            while e_util.is_prime(n**2 + a * n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                max_a = a
                max_b = b
    print max_a * max_b
    
if __name__ == '__main__':
    main()
