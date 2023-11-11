#1.1
print("** ** ******    **      **     ** ****" )
print("** ** **        **      **     **   **")
print("***** ******    **      **     **   **")
print("** ** **        **      **     **   **")
print("** ** ** ****   ******  ******  ******")



#1.3
ten_hang = "Sữa hộp Vinamilk"
so_luong = 5
don_gia = 25000
tien_phai_tra = so_luong * don_gia
print("Tên hàng:", ten_hang)
print("Số lượng:", so_luong)
print("Tiền phải trả:", tien_phai_tra)




#1.4
yeu_cau_1 = (5 - 3) // 2
print("(5-3)//2", "=", yeu_cau_1)
yeu_cau_2 = (8-3*2)-(1+1)
print("(8-3*2)-(1+1)", "=", yeu_cau_2)



#1.5
xây dựng tiền theo công thức
so_luong = int(input('nhập số lượng:'))
don_gia = int(input('nhập đơn giá:'))
print('thành tiền:',so_luong*don_gia)



#1.6
alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash = (alice_candies + bob_candies + carol_candies)%3
print("số kẹo dư bị đập là =", to_smash)


#1.7
do_C = int(input('nhập độ C:'))
print('độ F:',9/5*do_C+32)



#1.8
s1 = str(input('nhập chuỗi s1:'))
s2 = str(input('nhập chuỗi s2:'))
s3 = str(input('nhập chuỗi s3:'))
index = int(input('nhập index:'))
print('chiều dài của các chuỗi s1, s2 và s3 lần lượt là:',len(s1),len(s2),len(s3))
print('chuỗi s4:',s1[index:])
print('chuỗi s2 lặp lại 2 lần:',s2*2)



#1.9
lai_xuat_mot_nam = float(input('nhập lãi suất một năm:'))
so_tien_gui = int(input('nhập số tiền gửi:'))
so_thang_gui = int(input('nhập số tháng gửi:'))
so_tien_lai = (so_tien_gui*so_thang_gui)*(lai_xuat_mot_nam/100/12)
print('tiền lãi:',(so_tien_gui*so_thang_gui)*(lai_xuat_mot_nam/100/12))
print('tiền vốn + lãi:',so_tien_gui+so_tien_lai)
