def main():
    skip = 1
    p = 0
    diags = 1
    i = 1
    # create spiral
    while True:
        for _ in xrange(4):
            i += skip + 1
            if e_util.is_prime(i):
                p += 1
        diags += 4
        if float(p) / diags < .10:
            print skip + 2
            return
        skip += 2

if __name__ == '__main__':
    main()
