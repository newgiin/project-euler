def main():
    # TODO   
    for i in xrange(2, 10**8):
        if e_util.is_palindrome(str(i)):
            print i

if __name__ == '__main__':
    main()
