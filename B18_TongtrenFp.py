from math import log,ceil,floor
p = 2971215073
W = 8
m = log(p,2)
t = ceil(m/W)
print("Độ dài từ p: ",t)
e = [pow(2,W*i) for i in range(t)]
p1 = []
for i in e[::-1]:
    p1.append(floor(p/i))
    p = p%i
print("p = ", p1)
a = int(input("Nhập số a: "))
a1 = []
for i in e[::-1]:
    a1.append(floor(a/i))
    a = a%i
b = int(input("Nhập số b: "))
b1 = []
for i in e[::-1]:
    b1.append(floor(b/i))
    b = b%i
def ccxb(a,b,W,t):
    a.reverse()
    b.reverse()
    c = []
    e = pow(2,W)
    epsilon = 0
    for i in range(t):
        s = a[i] + b[i] + epsilon
        x = s%e
        if(s>e):
            epsilon = 1
        else: epsilon = 0
        c.append(x)
    c.reverse()
    return [epsilon, c]
def tcxb(a,b,W,t):
    a.reverse()
    b.reverse()
    c = []
    e = pow(2,W)
    epsilon = 0
    for i in range(t):
        d = a[i] - b[i] - epsilon
        if(d<0):
            epsilon = 1
            d += e
        else: epsilon = 0
        x = d%e
        c.append(x)
    exp = [pow(2,W*i) for i in range(t)]
    res = 0
    for i in range(t):
        res += c[i]*exp[i]
    return [epsilon, res]
if __name__ == '__main__':
    [epsilon, c] = ccxb(a1,b1,W,t)
    print([epsilon, c])
    if(epsilon == 1):
        s=tcxb(c,p1,W,t)
        print(s)
        s1 = []
        for i in e[::-1]:
            s1.append(floor(s[1]/i))
            s[1] = s[1]%i
        print(s1)
    else:
        c.reverse()
        p1.reverse()
        for i in range(t):
            if(c[i]>=p1[i]):
                c.reverse()
                p1.reverse()
                s=tcxb(c,p1,W,t)
        print(s)
        s1 = []
        for i in e[::-1]:
            s1.append(floor(s[1]/i))
            s[1] = s[1]%i
        print(s1) 