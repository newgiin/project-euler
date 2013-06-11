def main():
    result = []
    for i in xrange(2, 9999999):
        word = str(i)
        acc = 0
        for c in word:
            acc += int(c)**5
        if acc == i:
            result.append(i) 
    print sum(result)

if __name__ == '__main__':
    main()
