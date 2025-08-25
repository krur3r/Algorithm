#5. Viết chương trình tính tổng của các số nguyên tố nằm trong khoảng [A, B] với A, B nhập vào từ bàn phím.
from math import sqrt
a=int(input("Nhập số a: "))
b=int(input("Nhập số b: "))
def SoE(mprime,b):
    prime=[1 for i in range(a,b+1)]
    l=int(sqrt(b))
    for i in range(2,l+1):
        for j in range(i*i,l+1,i):
            prime[j]=0
    for p in range(2,l+1):
        if(prime[p]):
            mprime.append(p)
def SegmentedSoE(a,b):
    tong=0
    mprime = []
    SoE(mprime, b)
    prime=[1 for i in range(b-a+1)]
    for i in mprime:
        low=a//i
        if(low<=1):
            low=i+i
        elif((a%i)!=0):
            low=(low*i)+i
        else:
            low=low*i
        for j in range(low,b+1,i):
            prime[j-a]=0
    for p in range(a,b+1):
        if(prime[p-a]):
            print(p)
            tong+=p
    print(tong)
print(SegmentedSoE(a, b))   
   
