def main():
    f = open("e_13.in", "r")
    line = f.readline()
    # 2d array holding last 10 digits per line
    # must do it this way since Python has no easy way to make 2d arrays
    arr = [[], [], [], [], [], [], [], [], [], []]
    while line:
        arr[0].append(int(line[49]))
        arr[1].append(int(line[48]))
        arr[2].append(int(line[47]))
        arr[3].append(int(line[46]))
        arr[4].append(int(line[45]))
        arr[5].append(int(line[44]))
        arr[6].append(int(line[43]))
        arr[7].append(int(line[42]))
        arr[8].append(int(line[41]))
        arr[9].append(int(line[40]))
        line = f.readline()
    
    carry = 0
    result = "" 
    for place in xrange(10):
        sum = carry
        for digit in arr[place]:
            sum += digit
        ones = sum % 10
        result = str(ones) + result
        carry = int((sum - ones) / 10)
    print result

if __name__ == '__main__':
    main()
