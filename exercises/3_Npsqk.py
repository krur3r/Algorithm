# 3. Cho một số nguyên dương N, gọi:
# -	k là số ước nguyên tố của N;
# -	q là tổng của các ước nguyên tố của N;
# -	p là tổng của các ước số của N;
# -	s là số ước của N;
# Hãy viết chương trình tính giá trị của: N+p+s-q-k với N cho trước nhập từ bàn phím.
# Ví dụ: N=24, có các ước là {1,2,3,4,6,8,12, 24} do đó: 
# p=1+2+3+4+6+8+12+24=60 và s=8
# trong đó có 2 ước nguyên tố là {2,3} do đó:
# q=2+3=5 và k=2
# Và từ đó: N+p+s-q-k = 24+60+8-5-2=85;

N=int(input("Nhập n nguyên dương: "))
prime = [1 for i in range(N+1)]
p1=2
q=k=p=s=tong=0
while(p1*p1<=N):
    for i in range(p1*p1,N+1,p1):
        prime[i] = 0
    p1+=1
for i in range(2,N+1):
    if(prime[i]==1 and N%i==0):
        q=q+i
        k+=1
print("Tổng các ước nguyên tố của",N,":",q)
print("Số ước nguyên tố của",N,":",k)
for i in range(1,N+1):
    if(N%i==0):
        p=p+i
        s+=1
tong=N+p+s-q-k
print("Kết quả: ",tong)
