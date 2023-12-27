# Tổ chức và sử dụng module.
from ham_chuong_8 import *

# TÌm max and min 4 số nhập vào:
print("TÌm max and min 4 số nhập vào:")
while True:
    try:
        a = int(input("Nhập số nguyên: "))
        b = int(input("Nhập số nguyên: "))
        c = int(input("Nhập số nguyên: "))
        d = int(input("Nhập số nguyên: "))
        break
    except ValueError:
        print("Lỗi giá trị nhập vào!!")
print(find_max_min(a, b, c, d))
# Tính trụ tuyệt đố.
print("Tính giá trị tuyệt đối")
while True:
    try:
        x = eval(input("Nhập số: "))
        break
    except ValueError:
        print("Lỗi giá trị nhập vào")
    except NameError:
        print("Lỗi nameerror!!")
    except SyntaxError:
        print("Lỗi cú pháp!!!")
print(f"Trị tuyệt đối của {x} là:", ttd(x))
# Giải phương trình bậc nhất.
print("Giải phương trình bậc nhất")
while True:
    try:
        a = eval(input("Nhập hệ số a: "))
        b = eval(input("Nhập hệ số b: "))
        break
    except ValueError:
        print("Lỗi giá trị nhập vào!!")
    except NameError:
        print("Lỗi nameerror!!!")
    except SyntaxError:
        print("Lỗi cú pháp!!!")

print(gpt_bac1(a, b))
# Tính diện tích tam giác.
print("Tính diện tích tam giác")
while True:
    try:
        a = eval(input("Nhập cạnh a: "))
        b = eval(input("Nhập cạnh b: "))
        c = eval(input("Nhập cạnh c: "))
        break
    except (ValueError, NameError) as er:
        print("ERROR:", er)
    except SyntaxError:
        print("Lỗi cú pháp!!!")
print("Diện tích tam giác là:", dien_tich_tam_giac(a, b, c))
# Kiểm tra năm nhuận.
print("Kiểm tra năm nhuận")
while True:
    try:
        year = int(input("Nhập năm: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("Lỗi giá trị nhập vào!!!")
print(f"Năm {year} là:", ktr_nam(year))
# Tính cước taxi.
while True:
    try:
        loai_xe = input("Nhập loại xe(4 hoặc 7): ")
        khoang_cach = int(input("Khoảng cách: "))
        thoi_gian_cho = int(input("Thời gian chờ: "))
        break
    except (NameError, SyntaxError, TypeError, ValueError):
        print("Lỗi giá trị nhập vào")
print("Tiền phải trả là:", tinh_cuoc_taxi(loai_xe, khoang_cach, thoi_gian_cho))
# Tính tiền điện:
print("Tính tiền điện:")
while True:
    try:
        so = int(input("Nhập số điện: "))
        break
    except ValueError:
        print("Lỗi giá trị nhập vào!!")
print("Tiền phải trả là:", tinh_tien_dien(so))
# Tính tiền thuê phòng resort.
while True:
    try:
        loai_phong = input("Nhập loại phòng(1 -> 8): ")
        so_dem = int(input("Nhập số đêm: "))
        break
    except (ValueError, SyntaxError, NameError, TypeError):
        print("Lỗi giá trị nhập vào!!!")
print(tien_resort(loai_phong, so_dem))
# Chương trình count down.
while True:
    try:
        so = int(input("Nhập n: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("Lỗi giá trị nhập vào!!!")
print(count_down(so))


# Kiểm tra số nguyên tố.
print("Kiểm tra số nguyên tố:")
while True:
    try:
        so = int(input("Nhập số: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("Lỗi cú pháp!!!")
print(snt(so))
# Tính các biểu thức sau:
while True:
    try:
        n = int(input("Nhập số tinh bieu thuc: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("Lỗi cú pháp!!!")
print(bieu_thuc(n))

# Tinh tong n so nguyen nhap vao.
while True:
    try:
        n = int(input("Tinh tong may so: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("Loi cu phap nhap lai!!!")
print(tong_n_so_nguyen(n))
# Tinh tong cac so nhap vao va dung lai khi nhap 0.
print(tinh_so_nguyen())
# Tinh UCLN va BCLN cua a va b la.
while True:
    try:
        a = int(input("Nhap a: "))
        b = int(input("Nhap b: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("loi cu phap!!")
print(f"UCLN cua {a} va {b} la:", ucln(a, b))
print(f"BCLN cua {a} va {b} la:", bcln(a, b))
# Tim so hoan hao.
while True:
    try:
        so = int(input("Nhap so ktr so hoan hao hay khong: "))
        break
    except (ValueError, NameError, SyntaxError):
        print("loi cu phap!!")
print(so_hoan_hao(so))


# Đảo ngược số.
chain = input("Nhập dãy số: ")
print(dao_nguoc_so(chain))
