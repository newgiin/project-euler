def main():
    max = 0
    for i in xrange(2, 49877):
        ct_prd = ""
        m = 1
        while len(ct_prd) < 9:
            ct_prd += str(i * m)
            m += 1
        if e_util.is_perm(ct_prd, "123456789") and int(ct_prd) > max:
            max = int(ct_prd)
    print max    

if __name__ == '__main__':
    main()
