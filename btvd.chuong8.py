#8.1
print("Bài toán tìm số lớn nhất và nhỏ nhất.")
a=eval(input("Nhập số a:"))
b=eval(input("Nhập số b:"))
c=eval(input("Nhập số c:"))
d=eval(input("Nhập số d:"))
g=0
h=0
while(g<a)or(g<b)or(g<c)or(g<d):
    g+=1
h=g
while(h>a)or(h>b)or(h>c)or(h>c):
    h-=1
print("max =",g)
print("min =",h)        


#8.2
integer = -20
print('Giá trị tuyệt đối của -20 là:', abs(integer))
 
floating = -30.11
print('Giá trị tuyệt đối của -30.11 là:', abs(floating))



#8.3
a = 4
b = -8
x = -b/a
print(\"Nghiệm của phương trình là:\", x)


#8.4
import math
a=float(input("Nhập cạnh a:"))
b=float(input("Nhập cạnh b:"))
c=float(input("Nhập cạnh c:"))
p=((a+b+c)/2)
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print("Diện tích tam giác là", S)



#8.5
if (nam % 400 == 0) or ((nam % 4 == 0) and (nam % 100 != 0)):
    print('Nam nhuan')
else:
    print('Nam khong nhuan')




#8.6
loai_xe=int(input("Cho biết loại xe là 4/7 ?"))
so_km=float(input("Nhập số km chạy bằng = "))
time_cho=float(input("Cho biết thời gian chờ (phút chờ) = "))
tien_cuoc=float(0)
tien_di_chuyen=float(0)
if time_cho >=5:
    tien_cho=(time_cho-5)*0.8
else:
    tien_cho=0
if loai_xe==4:
    if so_km <=0.8:
        tien_di_chuyen=0.8*11000
    elif so_km <=20:
        tien_di_chuyen=0.8*11000+(20-so_km)*12100
    else:
        tien_di_chuyen=0.8*11000+(20-0.8)*12100+(so_km-20)*10000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 4 chỗ của quý khách là %0.2f"%tien_cuoc)
if loai_xe==7:
    if so_km <=0.8:
        tien_cuoc+tien_cho+0.8*13000
    elif so_km <=30:
        tien_cuoc=tien_cho+0.8*13000+(30-so_km)*14100
    else:
        tien_cuoc=tien_cho+0.8*13000+(30-0.8)*14100+(so_km-30)*12000
    tien_cuoc=tien_cho+tien_di_chuyen
    print("Cước phí xe taxi 7 chỗ của quý khách là %0.2f"%tien_cuoc)

#8.7
a=eval(input("Nhập số KWh tiêu thụ:"))
if a>=0:
    if a<=50:
       print("Tổng số tiền phải trả là:",a*1678,"đồng.")
    elif a<=100:
       print("Tổng số tiền phải trả là:",50*1678+(a-50)*1734,"đồng.")
    elif a<=200:
       print("Tổng số tiền phải trả là:",50*(1678+1734)+(a-100)*2014,"đồng.")
    elif a<=300:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014)+(a-200)*2536,"đồng.")
    elif a<=400:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536)+(a-300)*2834,"đồng.")
    else:
       print("Tổng số tiền phải trả là:",50*(1678+1734+2014+2536+2834)+(a-400)*2927,"đồng.")     
else:
   print("Số KWh không hợp lệ.")
    

#8.8
print("Các mã loại phòng cho bạn:")
print("1-Standard")
print("2-Superior Garden View")
print("3-Superior Ocean View")
print("4-Garden View Bungalow")
print("5-Pool View Bungalow")
print("6-Family Room")
print("7-Beach Front Bungalow")
print("8-VIP sea View")
a=eval(input("Nhập mã loại phòng:"))
b=eval(input("Nhập số đêm:"))
if a>0&a<=8:
    if a==1: c=1260000
    elif a==2: c=1550000
    elif a==3: c=1830000
    elif a==4: c=1830000
    elif a==5: c=2120000
    elif a==6: c=2120000
    elif a==7: c=2540000
    elif a==8: c=4800000
    else: 
        print("Vui lòng chọn lại mã loại phòng.")
else: print("Vui lòng chọn lại mã loại phòng.") 
if b==1:
    print("Giá  tiền phải trả là:",c,"đồng.")
elif b==2:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b==3:
    print("Giá  tiền phải trả là:",c*b*0.75,"đồng.") 
elif b>=4:
    print("Giá  tiền phải trả là:",c*b*0.7,"đồng.")       
else:
     print("Vui lòng nhập lại số đêm.")



#8.9
a = int(input("nhap so a: "))
for i in range(a,0,-1):
    print(i)



#8.10
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
s=(x*x+1)**n
print("(S=x*x+1)^n =",s)

#8.11
print("Nhập n:")
n=eval(input(""))
print("Nhập x:")
x=eval(input(""))
A=(x*x+x+1)**n + (x*x-x+1)**n
print("A=(x*x+x+1)^n+(x*x-x+1)^n=",A)



#8.12
def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, n):
        if n % i == 0: 
            return False  
    return True

n = int(input(">> nhap so tu nhien: "))

if is_prime(n):
    print(f"{n} la so nguyen to")
else:
    print(f"{n} khong phai so nguyen to")




#8.14
a = int(input("nhập số nguyên N: "))
b = 0
for i in range(1, a+1):
    print("nhập số hạng thứ:", i)
    b1 = int(input())
    b = b + b1
print("tổng",a,"số hạng là ", b)


#8.15
a = True
S = 0
while a:
    print("nhập số nguyên N: ")
    b = int(input())
    S = S + b
    if b ==0:
        a = False
        break
print("tổng số hạng vừa nhập là: ",S)



#8.16
def USCLN_1(a, b):
    if b == 0:
        return a
    return USCLN_1(b, a % b)


def USCLN_2(a, b):
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


a = int(input('Nhap vao so nguyen duong a = '))
b = int(input('Nhao vao so nguyen duong b = '))

print('Uoc so chung lon nhat cua a va b la: ', USCLN_1(a, b))
print('Uoc so chung lon nhat cua a va b la: ', USCLN_2(a, b))


#8.17
a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))
c = a*b
for i in range (b, c+1):
    if i%a == 0 and i%b == 0:
        d = i
        break
print(i)



#8.18
print("Nhập vào số N lớn hơn 0: ")
 
n = int(input())
tong = 0
 
for i in range(1, n):
    if (n % i == 0):
        tong += i
 
if (tong == n):
    print(n, " là số hoàn hảo")
else:
    print(n, " không phải là số hoàn hảo")


#8.19
def dao_nguoc_va_loai_bo_so_chan(danh_sach):
    danh_sach_dao_nguoc = danh_sach[::-1]  # Đảo ngược danh sách
    danh_sach_le = [x for x in danh_sach_dao_nguoc if x % 2 != 0]  # Loại bỏ các số chẵn
    return danh_sach_le

danh_sach_so = []
while True:
    so = input("Nhập số (Enter để kết thúc): ")
    if so == "":
        break
    so = int(so)
    danh_sach_so.append(so)

ket_qua = dao_nguoc_va_loai_bo_so_chan(danh_sach_so)
print("Dãy số lẻ đảo ngược:", ket_qua)

#8.20
def e_mu_x(x, sai_so, n=0, ket_qua=1):
    # Nếu sai số đã đạt được, hoặc n vượt quá một ngưỡng cố định (để tránh lặp vô hạn)
    if abs(x**n / factorial(n)) < sai_so or n > 100:
        return ket_qua
    else:
        n += 1
        ket_qua += x**n / factorial(n)
        return e_mu_x(x, sai_so, n, ket_qua)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

x = float(input("Nhập giá trị của x: "))
sai_so = 1e-4
ket_qua = e_mu_x(x, sai_so)
print(f"e^{x} gần đúng với sai số {sai_so} là: {ket_qua}")

