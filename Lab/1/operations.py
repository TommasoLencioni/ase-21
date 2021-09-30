#calculator.py

def sum(m,n):
    result=m
    negative=False
    if(n<0):
        negative=True
        n*=-1
    while n>0:
        if negative:
            result-=1
        else:
            result+=1
        n-=1
    return result

def efficient_sum(m,n):
    add_step = 1 if n>0 else -1
    for _ in range (abs(n)):
        m+=add_step
    return m

def divide(m,n):
    if n==0:
        return "Impossible"
    negative=(((m<0) and  not (n<0)) or (not (m<0) and (n<0)))
    i=-1
    m=abs(m)
    n=abs(n)
    while m>=0:
        m-=n
        i+=1
    if negative:
        return i*-1
    else:
        return i
