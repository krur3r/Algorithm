#7. Một số emirp là một số nguyên tố mà khi đảo ngược vị trí các chữ số của nó, ta cũng được một số nguyên tố. Viết chương trình liệt kê các số emirp nhỏ hơn N với N nhập vào từ bàn phím.
n=int(input("Nhập n: "))
def reverse(n):
    rev=0
    while(n>0):
        rev=(rev*10)+n%10
        n=n//10
    return rev
def emirp(n):
    prime=[1 for i in range(n+1)]
    p=2
    while(p*p<=n):
        for i in range(p*p,n+1,p):
            prime[i]=0
        p+=1
    for p in range(2,n+1):
        if(prime[p]==1):
            rev=reverse(p)
            if(p!=rev and prime[rev]==1 and rev<n):
                print(p)
emirp(n)
