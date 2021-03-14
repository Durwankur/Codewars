def digitize(n):
    n = str(n)
    a= list(n)[::-1]
    
    for i in range(len(a)):
        a[i] = int(a[i])
    return a
