def solution(st, limit): 
    s=[]
    sit= list(st)
    
    
    if len(st)<=limit:
        return (st)
    else:
        for i in range(0,limit):
            s.append(sit[i])
            
        e=""    
        se=e.join(s)
        
        
        if len(se)==len(sit):
            return (se)
        elif len(se)<len(sit):
            return (se + "...")
