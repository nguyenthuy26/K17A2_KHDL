#7.1:
print("Bài 7.1: Tính và in ra tổng của biểu thức S")
x=int(input("Nhập x:"))
S=1+x+x**3/3+x**5/5
print("S=1+x+x^3/3+x^5/5=", S)

#7.2
print("Tính kết quả 2")
result=1+2
print('result=', result)
original_result=result
result=result-1
print('result=', result)
original_result=result
result=result*2
original_result=result
print('result=', result)
result=result**3
original_result=result
print('result=', result)
result=result+8
original_result=result
print('result=', result)
result=result%7
original_result=result
print('result=', result)
result=result//2
original_result=result
print('result=', result)


#7.3
print("Tính kết quả 3")
result=5
print('result=', result)
result-=1
print('result=', result)
result+=3
print('result=', result)
result=-result
print('result', result)
result=True
print('not result=', not result)

#7.4
print("Tính kết quả 4")
x=10
y=4
print('x=%d, y=%d'%(x,y))
equivelence=x==y
print('x==y is', equivelence)
equivelence=x!=y
print('x!=y is', equivelence)

x=8
y=9
print('x=%d, y=%d'%(x,y))
equivelence=x>=y
print('x>=y is', equivelence)
equivelence=x<y
print('x<y is', equivelence)
equivelence=x<=y
print('x<=y is', equivelence)


#7.5
print("Tính kết quả 5")
x=15
y=12
print('Binary of x=', bin(x), 'Binary of y=', bin(y))
print('x&y=', bin(x&y))
print('x|y=', bin(x|y))
print('x^y=', bin(x^y))
print('~x=', bin(~x))
print('x<<2=', bin(x<<2))
print('y>>2=', bin(y>>2))

#7.7
x=int(input("Số tiền muốn đổi:"))
so_to_500000=x//500000
so_to_200000=x%500000//200000
so_to_100000=(x%500000%200000)//100000
so_to_50000=((x%500000%200000)%100000)//50000
tien_con_lai=x-(so_to_500000*500000+so_to_200000*200000+so_to_100000*100000+so_to_50000*50000)
print("Số tờ 500000:", so_to_500000)
print("Số tờ 200000:", so_to_200000)
print("Số tờ 100000:", so_to_100000)
print("Số tờ 50000:", so_to_50000)
print("Tiền còn lại:", tien_con_lai)
