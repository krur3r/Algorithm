from random import randint
def dec_to_bin(k):
    r = []
    while(k>0):
        k1 = k%2
        r.append(k1)
        k = k//2
    return r
def repeated_square(a,k,n):
    b=1
    k=dec_to_bin(k)
    if(k[0]==0):
        b = 1
    else: b = a
    A = a
    for i in k[1:]:
        A = (A*A)%n
        if(i==1):   b = (A*b)%n
    return b
def Miller_Rabin(n,t):
    if(n<2):
        return 0
    if(n==2 or n==3):
        return 1
    s=0
    r=n-1
    while(r%2==0):
        s+=1
        r//=2
    for _ in range(t):
        a=randint(2,n-2)
        y=repeated_square(a,r,n)
        if(y!=1 and y!=n-1):
            j=1
            while(j<=s-1 and y!=n-1):
                y=(y*y)%n
                if(y==1):
                    return 0
                j+=1
            if(y!=n-1):
                return 0
    return 1
def result(l,r):
    s=0
    for i in range(l,r):
        if(Miller_Rabin(i,i)==1):
            Fi=i
        else:
            Fi=0
        for j in range(i+1,r):
            if(Miller_Rabin(j,j)==1):
                Fj=j
            else:
                Fj=0
            s+=Fi*Fj
    return s
if __name__=='__main__':
    l=int(input("Nhập l: "))   
    r=int(input("Nhập r> l: "))
    print(result(l, r)) 
    