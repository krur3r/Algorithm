n=int(input("Nhập n: "))
def amicable_nums(n):
    for i in range(2,n):
        p=q=0
        N=i
        for j in range(1,N):
            if(N%j==0):
                p+=j
        for j in range(1,p):
            if(p%j==0):
                q+=j
        if(q==N and q!=p):   print("Cặp số thân thiết: ",p,N)
amicable_nums(n)