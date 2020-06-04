def is_leap(year):
    leap = False
    
    year = 2100
    print(year, year %100)
    # Write your logic here
    if year %100 == 0 :
        leap = False
    elif year %4 == 0 :
        leap = True
    
        
    elif year %400 == 0 :
        leap = True
    
    
    #     if year %4 == 0 :
    #     leap = True
    # elif year %100 == 0 :
    #     leap = False
        
    # elif year %400 == 0 :
    #     leap = True


    return leap

year = int(input())
print(is_leap(year))