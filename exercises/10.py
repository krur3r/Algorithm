#10. Viết chương trình đếm số ước và số ước nguyên tố của một số N nhập vào từ bàn phím.
n=int(input("Nhập n: "))
p=2
dem=demnt=0
prime=[1 for i in range(n+1)] #prime=1*(n+1)
while(p*p<=n):
    for i in range(p*p,n+1,p):
        prime[i]=0
    p+=1
for p in range(2,n+1):
    if(prime[p]==1 and n%p==0):
        demnt+=1
for i in range(1,n+1):
    if(n%i==0):
        dem+=1
print("Số ước: ",dem)
print("Số ước nguyên tố: ",demnt)
