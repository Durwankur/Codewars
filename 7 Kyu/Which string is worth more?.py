def highest_value(a, b):
    s1 = 0 
    s2 = 0
    for i in range(len(a)):
        s1 = s1 + ord(a[i])
    for j in range(len(b)):
        s2 = s2 + ord(b[j])
    return b if s2>s1 else a
