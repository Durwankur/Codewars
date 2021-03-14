def div_con(x):
    s = 0
    v= 0
    for i in range(len(x)):
        if type(x[i])== str:
            x[i]= int(x[i])
            s = s + x[i]
        else:
            v = v + x[i]
    return v-s
