def num_sums(n, terms, lwr_lim):
    if terms == 1:
        return 1
    result = 0
    for i in xrange(lwr_lim, n / terms + 1):
        rmdr = n - i
        result += num_sums(rmdr, terms - 1, i)
    return result
    
def main():
    n = 100
    result = 0
    for num_terms in xrange(2, n + 1):
        result += num_sums(n, num_terms, 1)
    print result
              
if __name__ == '__main__':
    main()
