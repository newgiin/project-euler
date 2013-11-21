def change_combos(n, denoms):
    a = [0] * (n+1)
    a[0] = 1
    for d in denoms:
        for i in xrange(d, n+1):
            a[i] += a[i-d]    
    return a[n]

def main():
    denoms = [1, 2, 5, 10, 20, 50, 100, 200]
    print change_combos(200, denoms)

if __name__ == '__main__':
    main()
