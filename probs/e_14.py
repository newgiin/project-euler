def main():
    occurence = 0
    maxlength = 0
    memoi = [0] * 1000000
    for curr in xrange(1000000):
        length = 1
        n = curr
        if memoi[n] != 0:
            length = memoi[n]
        else:
            while n > 1:
                if n < 1000000 and memoi[n] != 0:
                    length += memoi[n]
                    break
                if n % 2 == 0:
                    n = int(n / 2)
                else:
                    n = 3 * n + 1
                length += 1
        memoi[curr] = length
        if length > maxlength:
            maxlength = length
            occurence = curr
    print(str(occurence) + " | " + str(maxlength))    

if __name__ == '__main__':
    main()
