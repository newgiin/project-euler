def is_hepta(x):
    sol = e_util.solve_quad(5, -3, -2 * x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False    

def is_octa(x):
    sol = e_util.solve_quad(3, -2,  -x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False

def is_square(x):
    return math.sqrt(x) % 1 == 0
    
def check_fam(x):
    """
    Returns 0 if x is a triangle number, 1 if square, ... , 5 if octagonal.
    """
    func_arr = [is_triangle, is_square, is_penta, is_hexa, is_hepta, is_octa]
    for i in xrange(len(func_arr)):
        if func_arr[i](x):
            return i
    return None

def find_cyclic_chain(fam_map, x, fams_found):
    result = []
    # base case when x does not belong to a family or if we've already seen
    # this family.
    if x not in fam_map:
        return result
    if fams_found[fam_map[x]]:
        # all hexagonal numbers are also triangular
        if fam_map[x] == 0 and not fams_found[3]:
            fams_found[3] = True 
        else:
            return result
    result.append(x)
    fams_found[fam_map[x]] = True
    longest = []
    next_num = int(str(x)[-2 : ] + "00")
    # return longest possible chain
    # e.g. for numbers between 1800 to 1899
    for i in xrange(next_num, next_num + 100):
        chain = find_cyclic_chain(fam_map, i, list(fams_found))
        if len(chain) > len(longest):
            longest = chain
    return result + longest

def main():
    fam_map = {}
    for i in xrange(1000, 10000):
        fam = check_fam(i)
        if fam is not None:
            fam_map[i] = fam
    for i in fam_map:
        chain = find_cyclic_chain(fam_map, i, [False] * 6)
        if len(chain) == 6 and str(chain[len(chain) - 1])[-2 : ] \
                == str(i)[0 : 2]:
            print chain
            print sum(chain)
            return
        
if __name__ == '__main__':
    main()
