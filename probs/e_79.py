def main():
    f = open("keylog.txt", "r")
    visited = {}
    for line in f:
        line = line.strip() # remove newline
        for i in xrange(0, len(line)):
            c = line[i]
            if c not in visited:
                visited[c] = []
            for k in line[i + 1 : ]:
                if k not in visited[c]:
                    visited[c].append(k)    
    code = ""
    while len(visited) > 0:
        for c in visited: 
            if len(visited[c]) == len(visited) - 1:
                code += c
                del visited[c]
                break
    print code

if __name__ == '__main__':
    main()
