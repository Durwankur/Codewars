#Solution 1
def invert(lst):
    return [-x for x in lst]

#Solution 2
def invert(lst):
    for num in range(0,len(lst)):    
        lst[num]= -(lst[num])
    return lst
