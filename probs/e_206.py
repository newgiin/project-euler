def main():
    i = 1009000000
    i_s = str(i**2)
    template = ['2', '3', '4', '5', '6', '7', '8', '9', '0']
    while i_s[0] == '1':
        i += 1
        i_s = str(i**2)
        matched_all = True
        for j in xrange(len(template)):
            if template[j] != i_s[(j + 1) * 2]:
                matched_all = False
                break
        if matched_all:
            print i
            break

if __name__ == '__main__':
    main()
