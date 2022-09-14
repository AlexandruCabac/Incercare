import math
n=int(input())
m=int(input())
def ad(a,b):
    s=a+b
    return s
def pr(a,b):
    p=a*b
    return p
def med(a,b):
    k=(a+b)/2
    return k
def cmmd(a,b):
    loc1=[]
    loc2=[]
    comun={}
    for i in range(1,int(math.sqrt(n))):
        if(n%i==0):
            loc1.append(i)
    for i in range(1,int(math.sqrt(m))):
        if(m%i==0):
            loc2.append(i)
    for i in range(len(loc1)):
        if(loc1[i] in loc2):
            comun.add(loc1[i])
    for i in range(len(loc2)):
        if(loc2[i] in loc1):
            comun.add(loc2[i])
    a=comun[0]
def comp1(a,b):
    if(a<b):
        return a
    else:
        return b
def comp2(a,b):
    if(a>b):
        return a
    else:
        return b
def sum():
    q=int(input())
    w=int(input())
    print(q,"+",w,"=",q+w)
def pro():
    q=int(input())
    w=int(input())
    print(q,"*",w,"=",q*w)
