#8. Một số gọi là số Т-prime nếu nó có đúng 3 ước nguyên dương. Viết chương trình tìm các số Т-prime nhỏ hơn hoặc bằng N với N cho trước nhập từ bàn phím.
n=int(input("Nhập n: "))
def check_divisor(n):
    d=2
    for i in range(2,(n//2)+1):
        if(n%i==0):
            d+=1
    return d==3
if(n<=3):   print("No")
for i in range(n+1):
    if(check_divisor(i)==1):
        print(i)
        
