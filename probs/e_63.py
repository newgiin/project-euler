def main():
    digits = 1
    count = 1 # we know 1^x will always be 1 digit, so just count it here
    while True:
        i = 2
        pwrd = str(i**digits)
        while len(pwrd) <= digits:
            if len(str(pwrd)) == digits:
                count += 1
            i += 1
            pwrd = str(i**digits)
        if i == 10 and len(str(9**digits)) < digits:
            break
        digits += 1
    print count

if __name__ == '__main__':
    main()
