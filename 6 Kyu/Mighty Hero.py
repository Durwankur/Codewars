def multi(i):
    n=1
    j=1
    for j in range(2, i):
        n *= j
        j+=1
    return n
def count_of_heads(initial, multiplier, swings):
    b = initial-1+multiplier
    for i in range(3,swings+2):
        b = b - 1 + (multi(i) * multiplier)
    return b
