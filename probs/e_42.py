def is_triangle(x):
    sol = e_util.solve_quad(1, 1, -2 * x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False
    
def is_triangle_word(word):
    total = 0
    for c in word:
        total += ord(c) - 64
    return is_triangle(total)

def main():
    result = 0
    f = open(INPUT_DIR + "words.txt", "r")
    line = f.readline()
    words = line.split(",")
    for w in words:
        w = w.replace('"', '')
        if is_triangle_word(w):
            result += 1
    print result 

if __name__ == '__main__':
    main()
