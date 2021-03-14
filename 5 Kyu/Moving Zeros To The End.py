def move_zeros(array):
    arr = []
    zero = []
    
    for i in range(len(array)):
        if array[i] == 0 or array[i]== 0.0:
            if type(array[i])==int or type(array[i])== float:
                zero.append(array[i])
            else: arr.append(array[i])
        else:
            arr.append(array[i])
    
    return arr + zero
