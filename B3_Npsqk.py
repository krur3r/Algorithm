N=int(input("Nhập n nguyên dương: "))
prime = [1 for i in range(N+1)]
p1=2
q=k=p=s=tong=0
while(p1*p1<=N):
    for i in range(p1*p1,N+1,p1):
        prime[i] = 0
    p1+=1
for i in range(2,N+1):
    if(prime[i]==1 and N%i==0):
        q=q+i
        k+=1
print("Tổng các ước nguyên tố của",N,":",q)
print("Số ước nguyên tố của",N,":",k)
for i in range(1,N+1):
    if(N%i==0):
        p=p+i
        s+=1
tong=N+p+s-q-k
print("Kết quả: ",tong)