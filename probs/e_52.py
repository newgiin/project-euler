def main():
    i = 10
    while True:
        flag = True
        m = 2
        for m in xrange(2, 7):
           if not e_util.is_perm(str(i), str(i * m)):
                flag = False
                break
        if flag:
            print i
            break 
        i += 1
        
if __name__ == '__main__':
    main()
