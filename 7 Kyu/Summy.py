import math
def summy(string_of_ints):
    a=string_of_ints.split(" ")
    for i in range(0,len(a)):
        a[i] = int(a[i])
        
    sum_of_ints = sum(a)
    return sum_of_ints
