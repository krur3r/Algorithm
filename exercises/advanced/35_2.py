#35. Cài đặt thuật toán kiểm tra số nguyên tố Miller-Rabin in ra kết luận về 1 số nguyên dương N nhập vào từ bàn phím với xác suất kết luận tương ứng sau thuật toán. 
from random import randint
import math
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
        b=1
    else: b=a
    A=a
    for i in k[1:]:
        A = pow(A,2)%n
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
        a=17
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
if __name__ == '__main__':
    n=int(input("Nhập n: "))
    t=int(input("Nhập tham số an toàn t>=1: "))
    if(Miller_Rabin(n,t)==0):
        print("Hợp số")
        print(f'Xác suât KL : {1-math.pow(1/4,t)}')
    else:
        print("Nguyên tố")
        print(f'Xác suât KL : {1-math.pow(1/4,t)}')
        
