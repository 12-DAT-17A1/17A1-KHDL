print("SỬ DỤNG BIỂU THỨC LAMBDA ĐỂ TÍNH")
r = eval(input("Nhập r: "))
a = eval(input("Nhập a: "))
b = eval(input("Nhập b: "))
dien_tich1= lambda r: 3.14*r**2
chu_vi1=lambda r: 2*3.14*r
dien_tich2= lambda a,b: a*b
chu_vi2= lambda a,b: (a+b)*2
print("Diện tích hình tròn là:",dien_tich1(r))
print("Chu vi hình tròn là:",chu_vi1(r))
print("Diện tích hình chữ nhật là:",dien_tich2(a,b))
print("Chu vi hình chữ nhật là:",chu_vi2(a,b))




