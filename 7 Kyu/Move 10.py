def move_ten(st):
    d=[]
    for i in range(len(st)):
        c= ord(st[i])
    
        if c+10>122:
            b = 10 - (122 - c) 
            b = b % 26
            k = chr(96+b)
    
        else:
            k = chr(c + 10)

        d.append(k)

    t= "".join(d)
    return(t)
