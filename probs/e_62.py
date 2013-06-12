def main():
    P = 5
    i = 5
    cubed = i**3
    num_digits = len(str(cubed))
    cubes = []

    while True:
        # cache cubes with num_digits
        while len(str(cubed)) == num_digits:
            cubes.append(cubed)
            i += 1
            cubed = i**3
        
        for j in xrange(len(cubes) - P + 1):
            cube_perms = 1
            for k in xrange(j + 1, len(cubes)):
                if e_util.is_perm(str(cubes[j]), str(cubes[k])):
                    cube_perms += 1
            if cube_perms == P:
                print cubes[j]
                return
                
        num_digits = len(str(cubed))
        cubes = []
        
if __name__ == '__main__':
    main()
