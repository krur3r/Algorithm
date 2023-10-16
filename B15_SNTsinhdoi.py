n=int(input("Nhập n: "))
p=2
prime=[1 for i in range(n+1)]
while(p*p<=n):
    for i in range(p*p,n+1,p):
        prime[i]=0
    p+=1
seq_p=[]
for p in range(2,n):
    if(prime[p]==1):
        seq_p.append(p)
        p+=1
print(seq_p)
for i in range(1,len(seq_p)):
    check=seq_p[i]-seq_p[i-1]
    if(check==2):   print("Cặp SNT sinh đôi: ",seq_p[i-1],seq_p[i])     