def main():
    first = 0
    sec = 1
    n = 1
    while len(str(sec)) < 1000:
        temp = first
        first = sec
        sec += temp
        n += 1
    print n
    
if __name__ == '__main__':
    main()
