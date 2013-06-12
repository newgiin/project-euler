def main():
    SUN = 1; MON = 2;TUE = 3;WED  = 4; THU = 5; FRI = 6; SAT = 7; 
    year = 1901
    month = 1
    day = TUE

    sum = 0
    while year < 2001:
        month = 1
        while month <= 12:
            if month == 9 or month == 4 or month == 6 or month == 11:
                day += 1
                if day > SAT:
                    day = SUN
            elif month == 2:
                day -= 1
                if day < SUN:
                    day = SAT
            else:
                if day == SAT:
                    day = MON
                elif day == FRI:
                    day = SUN
                else:
                    day += 2
            if day == SUN:
                sum += 1
            month += 1
        year += 1
    
    print sum
    
if __name__ == '__main__':
    main()
