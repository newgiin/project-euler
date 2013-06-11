def main():
    for num in xrange(11, 99):
        if str(num)[1] == "0":
            continue
        for den in xrange(num + 1, 99):
            num_s = str(num)
            den_s = str(den)
            if den_s[1] == "0":
                continue
            for n_i in xrange(0, len(num_s)):
                for d_i in xrange(0, len(den_s)):
                    if num_s[n_i] == den_s[d_i]:
                        red_num = num_s[0 : n_i] + num_s[n_i + 1 : len(num_s)]
                        red_den = den_s[0 : d_i] + den_s[d_i + 1 : len(den_s)]
                        if float(int(red_num)) / int(red_den) == float(num) / den:
                            print num_s + " / " + den_s
             
if __name__ == '__main__':
    main()
