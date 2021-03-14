def add_length(a):
    s = list(a.split(" "))
    c= []
    for i in range(len(s)):
        b = str(len(s[i]))
        b= s[i] + " " +b
        c.append(b)
    return c
