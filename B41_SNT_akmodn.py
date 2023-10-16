from math import sqrt
a = int(input("Nhập số nguyên dương a: "))
k = int(input("Nhập số nguyên dương k: "))
n = int(input("Nhập số nguyên dương n: "))
if(a<=0 or a>=n or k<=0 or k>=n or n>=1000):
    raise ValueError("0<a,k<n<1000")
def dec_to_bin(k):
    r = []
    while(k>0):
        k1 = k%2
        r.append(k1)
        k = k//2
    return r
def repeated_square(a,k,n):
    b = 1
    if(k[0]==0):
        b = 1
    else: b = a
    A = a
    for i in k[1:]:
        A = pow(A,2)%n
        if(i==1):   b = (A*b)%n
    return b
def check_prime(n):
    if(n<2):
        return 0
    sqrt_n=int(sqrt(n))
    for i in range(2,sqrt_n+1):
        if(n%i==0):
            return 0
    return 1
if __name__=='__main__':
    k = dec_to_bin(k)
    sq=repeated_square(a,k,n)
    print(sq)
    if(check_prime(sq)):
        print(sq,"là số nguyên tố")
    else:
        print(sq,"không phải là số nguyên tố")