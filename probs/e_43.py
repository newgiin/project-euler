def main():
    sum = 0
    primes = e_util.primes(18)
    for p in e_util.perms("0123456789"):
        flag = True
        for i in xrange(1, 8):
            if int(p[i : i + 3]) % primes[i - 1] != 0:
                flag = False
                break    
        if flag:
            sum += int(p)
    print sum

if __name__ == '__main__':
    main()
