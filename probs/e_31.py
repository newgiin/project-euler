def main():
    denoms = [1, 2, 5, 10, 20, 50, 100, 200]

    def combo_recurr(n, max_denom):
        if max_denom == 1:
            return 1
        remainder = n - max_denom
        if remainder == 0:
            return 1 + combo_recurr(n, denoms[denoms.index(max_denom) - 1])
        if remainder < 0:
            return combo_recurr(n, denoms[denoms.index(max_denom) - 1])
        return combo_recurr(remainder, max_denom) + combo_recurr(n, denoms[denoms.index(max_denom) - 1])
    
    def combos(n):
        return combo_recurr(n, 200)
    
    
    print combos(200)

if __name__ == '__main__':
    main()
