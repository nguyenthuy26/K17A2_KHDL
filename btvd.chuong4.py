#Bài 1
#Bước 1: Nhập x
#Bước 2: Gán a=x^2
#Nếu x>0 -> in ra bình phương của nó
#Nếu x<0 -> yêu cầu nhập số dương
#Bước 3: Kết thúc thuật toán
x=int(input("Nhập x:"))
a=x*x
if(x>0):
  print("Bình phương của x là:", a)
else:
  print("Bạn hãy nhập số dương")

#Bài 2
#Bước 1: Nhập số tự nhiên N
#Bước 2: Sử dụng lệnh for i in range (1, N+1)
#Bước 3: In ra các số nguyên từ 1 đến N
N=int(input("Nhập số tự nhiên N:"))
for i in range(1,N+1):
    print(i)

#Bài 3
#Bước 1: Nhập 2 số tự nhiên m, n
#Bước 2: Xét điều kiện
#Nếu đúng: sử dụng lệnh for i in range (1,n) và in ra i nếu i%m==0
#Nếu sai: yêu cầu nhập m<n
m=int(input("Nhập m:"))
n=int(input("Nhập n:"))
if(m<n):
          for i in range(1,n):
                    if(i%m==0):
                            print(i)
else:
        print("Bạn hãy nhập m<n")



#Bài 4
#Bước 1: Nhập 3 số a, b, c
#Bước 2: Lấy a và b so sánh với nhau
#Nếu a<b -> tiếp tục so sánh b với c. Nếu b<c: c lớn nhất; Nếu b>c: b lớn nhất
#Nếu a>b -> tiếp tục so sánh a với c. Nếu a<c: c lớn nhất; Nếu a>c: a lớn nhất
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
c=int(input("Nhập c:"))
if(a<b):
          if(b<c):
                  print("Số lớn nhất là:", c)
          else:
                  print("Số lớn nhất là:", b)
else:
        if(a<c):
                print("Số lớn nhất là:", c)
        else:
                print("Số lớn nhất là:", a)


#Bài 5
#Bước 1: Nhập 2 số a,b
#Bước 2: So sánh 2 số a,b và chọn ra số lớn hơn gán cho BCNN
#Bước 3: Nếu BCNN chia hết cho a và b -> in BCNN - kết thúc thuật toán
#Bước 4: Nếu BCNN không chia hết: tăng BCNN 1 đơn vị và quay lại bước 3
#Bước 5: In BCNN - kết thúc thuật toán
a=int(input("Nhập a:"))
b=int(input("Nhập b:"))
def bscnn(a, b):
    return int(a * b);
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b));

#Bài 7
#Bước 1: Nhập N
#Bước 2: Tính tổng các chữ số trong N
#Bước 3: In ra tổng các chữ số trong N - kết thúc thuật toán
def  totalDigitsOfNumber(n):
          total=0;
          while(n>0):
                    total=total+n%10;
                    n=int(n/10); 
          return total;
n=int(input("Nhập số nguyên dương n="));
print("Tổng các chữ số của", n, "là", totalDigitsOfNumber(n));
