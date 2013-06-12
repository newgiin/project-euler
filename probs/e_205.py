def main():
    wins = 0
    total = 0
    m = {}
    pete_sums = map(sum, e_util.repeat_perms([1,2,3,4], 9))
    colin_sums = map(sum, e_util.repeat_perms([1,2,3,4,5,6], 6))
    for pete in pete_sums:
        if pete in m:
            wins += m[pete]
        else:
            c = 0
            for colin in colin_sums:
               if pete > colin:
                    c += 1
            wins += c
            m[pete] = c
            
    print float(wins) / (len(pete_sums) * len(colin_sums))   

if __name__ == '__main__':
    main()
