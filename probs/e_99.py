def main():
    curr_line = max_line = max_base = max_exp = 0
    
    f = open(INPUT_DIR + "base_exp.txt", "r")
    for line in f:
        curr_line += 1
        exp_pair = line.split(",")
        curr_base = int(exp_pair[0])
        curr_exp = int(exp_pair[1])
        
        if curr_base > max_base**(float(max_exp) / curr_exp):
            max_base = curr_base
            max_exp = curr_exp
            max_line = curr_line
    print str(max_line)
    
if __name__ == '__main__':
    main()
