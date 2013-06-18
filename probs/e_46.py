def is_sumPrimeAndDouble(x, primes=e_util.get_primes(1000000)):
    p = primes[0]
    i = 0
    while p < x: 
        sum = 0
        base = 1
        while sum < x:
            sum = p + 2 * base**2
            base += 1
        if sum == x:
            return True   
        i += 1
        p = primes[i]
    return False

def main():
    i = 9
    primes = e_util.get_primes(10000)
    while True:
        if not e_util.is_prime(i) and not is_sumPrimeAndDouble(i, primes):
            print i
            return  
        i += 2
    
if __name__ == '__main__':
    main()
