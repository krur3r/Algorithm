def SoE(n):
    prime = [1 for i in range(n+1)]
    p=2
    while(p*p<=n):
        for i in range(p*p,n+1,p):
            prime[i] = 0
        p+=1
    prime1=[]
    for i in range(2,n+1):
        if(prime[i]==1):
            prime1.append(i)
    return prime1
def expression_prime(a,b,c,n):
    r=[]
    s=SoE(a*n*n+b*n+c)
    for x in range(1,n+1):
        value=a*x*x+b*x+c
        if value in s:
            r.append(x)
    return r
if __name__=='__main__':
    n=int(input("Nhập n: "))
    A=int(input("Nhập A: "))
    B=int(input("Nhập B: "))
    C=int(input("Nhập C: "))
    result=expression_prime(A,B,C,n)
    if len(result) > 0:
        print(result)
    else:
        print("Không có x thỏa mãn")