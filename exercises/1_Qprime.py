#1. Một số gọi là Q-prime khi nó có đúng 4 ước số nguyên dương. Hãy viết chương trình in ra các số Q-Prime nhỏ hơn hoặc bằng một số N cho trước nhập từ bàn phím.
def check_divisor(n):
    d=2
    for i in range(2,(n//2)+1):
        if(n%i==0):
            d+=1
    return d==4
n = int(input("Nhập n: "))
if(n==3):   print("No")
for i in range(n+1):
    if(check_divisor(i)):
        print(i)
