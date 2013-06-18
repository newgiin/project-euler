def main():
    max = 0
    max_sum = 0
    primes = e_util.get_primes(5000)
    prime_set = set(e_util.get_primes(1000000))
    for i in xrange(0, len(primes)):
        sum = primes[i]
        seq_len = 1
        for j in xrange(i + 1, len(primes)):
            sum += primes[j]
            if sum > 1000000:
                sum -= primes[j]
                break
            if sum in prime_set:
                seq_len = j - i + 1
        if seq_len > max:
            max = seq_len
            max_sum = sum
    print max_sum

if __name__ == '__main__':
    main()
