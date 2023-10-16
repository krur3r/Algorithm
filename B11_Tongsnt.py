n=int(input("Nhập n: "))
p=2
s=0
prime=[1 for i in range(n+1)]
while(p*p<=n):
    for i in range(p*p,n+1,p):
        prime[i]=0
    p+=1
for p in range(2,n+1):
    if(prime[p]==1):
        s+=p
print(s)