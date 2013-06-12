def main():
    f = open("triangle.txt", "r")
    arr = []
    for line in f:
        row = [int(num) for num in line.split()]
        arr.append(row)
    
    for row in xrange(1, len(arr)):
        arr[row][0] += arr[row - 1][0]
        for i in xrange(1, len(arr[row]) - 1):
            if arr[row - 1][i - 1] > arr[row - 1][i]:
                arr[row][i] += arr[row - 1][i - 1]
            else:
                arr[row][i] += arr[row - 1][i]
        arr[row][len(arr[row]) - 1] += arr[row - 1][len(arr[row - 1]) - 1]
    print max(arr[len(arr) - 1])
    
if __name__ == '__main__':
    main()
