from math import log, sqrt
def isPP(n):
    n = int(n)
    if n < 4: return None
    sr = round(sqrt(n),6)
    if sr == round(sr): return [sr, 2]
    a= int(n/2)
    for m in range(2,a):
        k = round(log(n, m),6)
        if k == round(k): return [m, k]
    return None
