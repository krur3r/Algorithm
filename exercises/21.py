#21. Một số gọi là siêu số nguyên tố nếu số lượng các số nguyên tố từ 1 đến X (ngoại trừ X) là một số nguyên tố. Hãy viết chương trình đếm số lượng các siêu số nguyên tố này trong khoảng [A,B] cho trước nhập từ bàn phím.
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
    if n < 2:
        return 0
    if n == 2 or n == 3:
        return 1
    s=0
    r=n-1
    while(r%2==0):
        s+=1
        r//=2
    for _ in range(t):
        a=randint(2,n-2)
        y=repeated_square(a,r,n)
        if(y==1 or y==n-1):
            continue
        for _ in range(s-1):
            y=(y*y)%n
            if(y==n-1):
                break
        else:
            return 0
    return 1
def s_prime(a,b):   
    super_p=[]
    for x in range(a,b+1):
        count=0
        for i in range(2,x):
            if(Miller_Rabin(i,i) and i%2!=0 or i==2):
                count+=1
        if(Miller_Rabin(count,count) and count%2!=0 or count==2):
            super_p.append(x)
    return super_p
if __name__=='__main__':
    a=int(input("Nhập a: "))
    b=int(input('Nhập b>a: '))
    result=s_prime(a,b)
    print(result)
    print("Có",len(result),"số siêu nguyên tố")
    
