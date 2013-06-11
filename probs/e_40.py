def main():
    d_end = 0
    d = 1
    p = 0
    result = 1
    while d <= 1000000:
        d_beg = d_end + 1
        r = 10**p
        len_r = len(str(r))
        i_beg = 10**p
        i_end = 10**(p + 1) - 1
        d_end = d_beg + len_r * 9 * r - 1
        while d >= d_beg and d <= d_end:
            d_cell = (d - d_beg) / len_r
            num = i_beg + d_cell     
            digit = str(num)[(d - d_beg) % len_r]
            result *= int(digit)
            d *= 10
        p += 1
    print result
        
if __name__ == '__main__':
    main()
