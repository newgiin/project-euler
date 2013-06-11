def main():
    total = 0
    for n in xrange(23, 101):
        for r in xrange(2, n):
            combos = e_util.factorial(n) / (e_util.factorial(r) * e_util.factorial(n - r))
            if combos > 1000000:
                total += 1
    print total 

if __name__ == '__main__':
    main()
