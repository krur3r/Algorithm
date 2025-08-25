#2. Viết chương trình tìm các số nguyên tố có N chữ số với N nhập từ bàn phím và 2 ≤ N ≤10.
n = int(input("Nhập số chữ số n: "))
if(n<2 or n>10):
    raise ValueError("Vui lòng nhập số n 2<=n<=10")
d=pow(10,n-1)
n=pow(10,n)-1
a=[1 for i in range(n+1)]
p=2
for i in range(d,n+1):
    while(p*p<=n):
        for i in range(p*p,n+1,p):
            a[i]=0
        p+=1
for p in range(d,n+1):
    if(a[p]):
        print(p)
