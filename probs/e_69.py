def main():
    max = 0
    max_n = 0
    for n in xrange(6, 1000001, 6):
        r = float(n) / totient(n)
        if r > max:
            max = r
            max_n = n
            print n
    print max_n 

if __name__ == '__main__':
    main()
