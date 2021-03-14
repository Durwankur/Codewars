def max_redigit(num):
    num = str(num)
    x = list(num)
    if len(x)!= 3 or int(num)<0:
        return None
    else:
        x.sort(reverse=True)
        return int("".join(x))
