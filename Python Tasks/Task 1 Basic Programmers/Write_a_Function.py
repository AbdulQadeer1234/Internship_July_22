def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year%400 == 0):
        leap = True
        return leap
    elif year%100==0:
        leap = False
        return leap
    elif year%4==0:
        leap = True
        return leap
    return leap

year = int(input())
print(is_leap(year))