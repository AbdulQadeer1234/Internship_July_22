def average(array):
    # your code goes here
    s=set()
    res=0
    for i in array:
        s.add(i)
    for i in s:
        res +=i
    
    return res/len(s)
