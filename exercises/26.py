# 26.  Một số được gọi là số S-num khi nó đồng thời vừa chia hết cho số nguyên tố và chia hết cho bình phương của số nguyên tố đó. Tìm số S-num nhỏ hơn số N cho trước (N < 10000).
from math import sqrt
def check_prime(n):
    if(n<2):
        return 0
    if(n==2):
        return 1
    for i in range(2,int(sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
if __name__=='__main__':
    n=int(input("Nhập n: "))
    for i in range(1,n):
        for j in range(2,int(sqrt(n))+1):
            if(check_prime(j)):
                if(i%j==0 and i%(j*j)==0):
                    print(i)
                    
