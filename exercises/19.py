#19. Viết chương trình in ra các số nguyên dương x nằm trong khoảng [n,m] sao cho giá trị của biểu thức Ax^2+Bx+C là một số nguyên tố. Với A,B,C, n,m là các số nguyên nhập từ bàn phím (n<m).
def SoE(m):
    p=2
    prime = {x: 1 for x in range(2, m+ 1)}
    while p <= m:
        for i in range(p,m+ 1):
            if p * i <= m and p * i in prime:
                del prime[p * i]
        p += 1
    return list(prime)
def expression_prime(a,b,c,n,m):
    r=[]
    s=SoE(a*m*m+b*m+c)
    for x in range(n,m+1):
        val=a*x*x+b*x+c
        if val in s:
            r.append(x)
    return r
if __name__=='__main__':
    n=int(input("Nhập n: "))
    m=int(input("Nhập m: "))
    if(n<m):
        A=int(input("Nhập A: "))
        B=int(input("Nhập B: "))
        C=int(input("Nhập C: "))
        result= expression_prime(A,B,C, n, m)
        if len(result)>0:
            print(result)
        else:   print("Không có x thỏa mãn")
    else:   print("Nhập n<m")
