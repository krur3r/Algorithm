def gcd(a,b):
    while(b>0):
        r = a%b
        a = b
        b = r
    return a
def compare(m,n,d):
    result=[]
    for i in range(m,n+1):
        for j in range(m,n+1):
            if(gcd(i,j)==d):
                result.append((i,j))
    return result
if __name__=='__main__':
    m=int(input("Nhập m: "))
    if(m>0 and m<1000):
        n=int(input("Nhập n: "))
        if(n>0 and n<1000):
            d=int(input("Nhập d: "))
            if(d>0 and d<1000):
                print(compare(m, n, d))
            else:
                print("Nhập 0<d<1000")
        else:
                print("Nhập 0<n<1000")
    else:
                print("Nhập 0<m<1000")               