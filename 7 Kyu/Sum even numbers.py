def sum_even_numbers(seq): 
    a=[]
    for i in range(len(seq)):
        if seq[i]%2 == 0:
            a.append(seq[i])
    return sum(a)
