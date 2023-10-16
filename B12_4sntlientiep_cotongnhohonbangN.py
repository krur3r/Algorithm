from math import sqrt
n=int(input("Nhập n: "))
p=2
check=1
seq_prime=[]
prime=[1 for i in range(n+1)]
while(p*p<=n):
    for i in range(p*p,n+1,p):
        prime[i]=0
    p+=1
for p in range(2,n+1):
    if(prime[p]==1):
        seq_prime.append(p)
print(seq_prime)
for j in range(seq_prime[-1]):
    s=seq_prime[j]+seq_prime[j+1]+seq_prime[j+2]+seq_prime[j+3]
    for k in range(2,int(sqrt(s))+1):
        if(s%k==0): check=0
    if(check==1):   print(seq_prime[j],seq_prime[j+1],seq_prime[j+2],seq_prime[j+3])
    else: break
    