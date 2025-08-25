#16. Viết chương trình tìm các số nguyên tố từ một mảng sinh ngẫu nhiên có kích thước N, với N nhập vào từ bàn phím.
from random import randint
def dec_to_bin(k):
    r = []
    while(k>0):
        k1 = k%2
        r.append(k1)
        k = k//2
    return r
def bin_to_dec(k):
    n=0
    exp=1
    for i in reversed(range(len(k))):
        n+=exp*k[i]
        exp*=2
    return n
def repeated_square(a,k,n):
    b=1
    k=dec_to_bin(k)
    if(k[0]==0):
        b = 1
    else: b = a
    A = a
    for i in k[1:]:
        A = pow(A,2)%n
        if(i==1):   b = (A*b)%n
    return b
def Miller_Rabin(n,t):
    s,r=0,n-1
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
def random_odd_kbits(bits):
    B=[0]*bits
    B[0]=1
    B[-1]=1
    for i in range(1,bits-1):
        B[i]=randint(0,1)
    return bin_to_dec(B)  
k=int(input("Nhập k-bits: "))
t=int(input("Nhập tham số an toàn t>=1: "))
while True:
    kbits=random_odd_kbits(k)
    if(Miller_Rabin(kbits,t)):
        print(kbits)
        break
