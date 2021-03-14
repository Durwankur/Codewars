def fake_bin(x):
    s = list(x)
    for i in range(len(s)):
        s[i] = int(s[i])
    for j in range(len(s)):
        if s[j] < 5:
            s[j]= 0
        else: 
            s[j] = 1
    for k in range(len(s)):
        s[k] = str(s[k])
    a= "".join(s)
    return a
