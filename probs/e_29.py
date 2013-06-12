def main():
    all = set(i**j for i in xrange(2, 101) for j in xrange(2, 101)) 
    print len(all)

if __name__ == '__main__':
    main()
