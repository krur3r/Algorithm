import random
def dec_to_bin(k):
    r = []
    while(k>0):
        k1 = k%2
        r.append(k1)
        k = k//2
    return r
def repeated_square(a,k,n):
    b=1
    k=dec_to_bin(k)
    if(k[0]==0):
        b = 1
    else: b = a
    A = a
    for i in k[1:]:
        A = (A*A)%n
        if(i==1):   b = (A*b)%n
    return b
def Miller_Rabin(n, t): 
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    s = 0
    x = n - 1
    while x % 2 == 0:
        s += 1
        x //= 2
    r = x
    for _ in range(1, t + 1):
        a = random.randint(2, n - 2)
        y = repeated_square(a, r, n)
        if y != 1 and y != n - 1:
            j = 1
            while j <= s - 1 and y != n - 1:
                y = y ** 2 % n
                if y == 1:
                    return False
                j += 1
            if y != n - 1:
                return False
    return True
def s_prime(a,b):   
    super_p=[]
    for x in range(a,b+1):
        count=0
        for i in range(2,x):
            if(Miller_Rabin(i,i) and i%2 != 0 or i==2):
                count+=1
        if(Miller_Rabin(count,count) and count%2 != 0 or count==2):
            super_p.append(x)
    return super_p
if __name__=='__main__':
    a=int(input("Nhập a: "))
    b=int(input('Nhập b>a: '))
    result=s_prime(a,b)
    print(result)
    print(len(result))
    