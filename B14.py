from math import sqrt
def reverse(n):
    rev=0
    while(n>0):
        rev=(rev*10)+n%10
        n//=10
    return rev
for i in range(100,1000):
    check=1
    for j in range(2,int(sqrt(i))):
        if(i%j==0):
            check=0
    if(check==1):
        rev=reverse(i)
        for z in range(1,int(sqrt(rev))+1):
            if(z*z*z==rev):
                print("Số cần tìm là:",i)
                print("Đảo ngược của",i,":",rev,"là lập phương của",z)
                