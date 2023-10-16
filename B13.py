from math import sqrt
n=int(input("Nhập n: "))
def check_prime(n):
    sqrt_n=int(sqrt(n))
    for i in range(2,sqrt_n+1):
        if(n%i==0):
            return 0
    return 1
for i in range(2,n+1):
    if(check_prime(i)==1):
        for j in range(i,n+1):
            if(check_prime(j)==1):
                tong=i+j
                hieu=abs(i-j)
                if(check_prime(tong)==1 and check_prime(hieu)==1):
                    print(i,j)