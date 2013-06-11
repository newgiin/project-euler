def is_penta(x):
    sol = e_util.solve_quad(3, -1,  -2 * x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False

def is_hexa(x):
    sol = e_util.solve_quad(2, -1,  -x)[1]
    if sol != None and sol > 0 and sol % 1 == 0:
        return True
    return False
    
def main():
    n = 286
    tri = n * (n + 1) / 2  
    while not (is_penta(tri) and is_hexa(tri)):
       n += 1
       tri = n * (n + 1) / 2
    print tri 

if __name__ == '__main__':
    main()
