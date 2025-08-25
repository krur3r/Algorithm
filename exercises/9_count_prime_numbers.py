#9. Viết chương trình đếm số số nguyên tố nhỏ hơn hoặc bằng N với N được nhập vào từ bàn phím.
n=int(input("Nhập n: "))
p=2
prime=[1 for i in range(n+1)] #prime=[1]*(n+1)
while(p*p<=n):
    for i in range(p*p,n+1,p):
        prime[i]=0
    p+=1
count=0
for i in range(2,n+1):
    if(prime[i]==1):
        count+=1
print(count)
