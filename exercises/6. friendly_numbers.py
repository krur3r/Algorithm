#6. Hai số tạo thành một cặp số thân thiết khi chúng tuân theo quy luật: Số này bằng tổng tất cả các ước của số kia (trừ chính số đó) và ngược lại. Viết chương trình tìm hai số dạng này nhỏ hơn N (với N nhập vào từ bàn phím).
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
