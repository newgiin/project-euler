def main():
    i = 1000
    T = 4 # find first T consecutive integers with T distinct factors
    i_processed = False # optimization to avoid getting prime factors twice
    while True:
        if i_processed or len(e_util.get_prime_factors(i)) >= T:
            seq_len = 1
            for j in reversed(xrange(1, T)): 
                if len(e_util.get_prime_factors(i + j)) >= T:
                    seq_len += 1
                else:
                    break
            if seq_len == T:
                print [i + k for k in xrange(0, T)]
                return
            i += T - seq_len + 1 # skip ahead 
            if seq_len > 1:
                i_processed = True
            else:
                i_processed = False
        else:
            i += 1 
            i_processed = False

if __name__ == '__main__':
    main()
