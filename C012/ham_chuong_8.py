from math import *


# Tìm só lớn nhất và số nhỏ nhất của 4 số nhập vào.
def find_max_min(a, b, c, d):
    lst = [a, b, c, d]
    return f"Max là: {max(lst)}\nMin là: {min(lst)}"


# Tính trụ tuyệt đố.
def ttd(a):
    return abs(a)


# Gpt bâc 1.
def gpt_bac1(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    x = -b / a
    return "Phương trình có nghiệm là: x =" + str(x)


# Tính diện tích tam giác.
def dien_tich_tam_giac(a, b, c):
    ncv = (a + b + c) / 2
    if (a + b > c) or (a + c > b) or (b + c > a):
        dien_tich = sqrt(ncv * (ncv - a) * (ncv - b) * (ncv - c))
        kq = round(dien_tich, 2)
        return float(kq)
    else:
        return "Đây không phải là một tam giác"


# Kiểm tra năm nhuận.
def ktr_nam(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "Năm nhuận"
    else:
        return "Năm không nhuận"


# Tính cước taxi.
# Tính cước taxi cho xe 4 chỗ và 7 chỗ với giá mỗi km
def tinh_cuoc_taxi(loai_xe, khoang_cach, thoi_gian_cho):
    thong_tin_cuoc = {
        "4": {
            "cuoc_codinh": 5,
            "don_gia_khoang_cach": 2.5,
            "don_gia_thoi_gian_cho": 0.5,
            "gia_moi_km": 1.2,
        },
        "7": {
            "cuoc_codinh": 7,
            "don_gia_khoang_cach": 3,
            "don_gia_thoi_gian_cho": 0.6,
            "gia_moi_km": 1.5,
        },
    }

    if loai_xe in thong_tin_cuoc:
        cuoc = (
            thong_tin_cuoc[loai_xe]["cuoc_codinh"]
            + thong_tin_cuoc[loai_xe]["don_gia_khoang_cach"] * khoang_cach
            + thong_tin_cuoc[loai_xe]["don_gia_thoi_gian_cho"] * thoi_gian_cho
            + thong_tin_cuoc[loai_xe]["gia_moi_km"] * khoang_cach
        )
        return cuoc
    else:
        return "Không có thông tin cước cho loại xe này"


# Tính tiền điện.
def tinh_tien_dien(so):
    gia1, gia2, gia3, gia4, gia5, gia6 = 1.678, 1.734, 2.014, 2.536, 2.834, 2.927
    if 0 <= so <= 50:
        tien = so * gia1
    elif so <= 100:
        tien = (50 * gia1) + (so - 50) * gia2
    elif so <= 200:
        tien = (50 * gia1) + (50 * gia2) + (so - 100) * gia3
    elif so <= 300:
        tien = (50 * gia1) + (50 * gia2) + (100 * gia3) + (so - 200) * gia4
    elif so <= 400:
        tien = (
            (50 * gia1) + (50 * gia2) + (100 * gia3) + (200 * gia4) + (so - 300) * gia5
        )
    else:
        tien = (
            (50 * gia1)
            + (50 * gia2)
            + (100 * gia3)
            + (200 * gia4)
            + 300 * gia5
            + (so - 400) * gia6
        )
    return tien


# Tính tiền thuê phòng resort.
def tien_resort(loai_phong, so_dem):
    thong_tin = {
        "1": 1260000,
        "2": 1550000,
        "3": 1830000,
        "4": 1830000,
        "5": 2120000,
        "6": 2120000,
        "7": 2540000,
        "8": 4480000,
    }
    if 2 <= so_dem <= 3:
        tien = (thong_tin[loai_phong] - (thong_tin[loai_phong] * 0.3)) * so_dem
        return "Số tiền phải trả là: {:,}".format(tien)

    else:
        tien = (thong_tin[loai_phong] - (thong_tin[loai_phong] * 0.3)) * so_dem
        return "Số tiền phải trả là: {:,}".format(tien)


# Chương trình count down.
def count_down(so):
    for i in range(so, 0, -1):
        print(i)
    return "Start!!!"


# Kiểm tra số nguyên tố.
def snt(so):
    if so <= 1:
        return "Không phải số nguyên tố"
    for i in range(2, int(so**0.2)):
        if so % i == 0:
            return "Không phải số nguyên tố"
    return "Là số nguyên tố"


# Tính và in ra các kết quả của các biểu thức sau.
def bieu_thuc(n):
    tong1 = 0
    for i in range(1, n + 1):
        if i % 2 != 0:
            tong1 += i
    tong2 = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong2 += i
    tich1 = 1
    for i in range(1, n + 1):
        tich1 *= i
    tich2 = 1
    for i in range(1, n + 1):
        if i % 3 == 0:
            tich2 *= i

    def snt(so):
        if so <= 1:
            return False
        for i in range(2, so):
            if so % i == 0:
                return False
        return True

    tong3 = 0
    for i in range(1, n + 1):
        if snt(i):
            tong3 += i
    tong4 = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            tong4 += -1 / i
        else:
            tong4 += 1 / i

    return f"""
    Tổng các số lẻ nhỏ hơn hay bằng {n} là: {tong1}      
    Tổng các số chẵn nhở hơn hay bằng {n} là: {tong2}     
    Tích các số từ 1 cho đến {n} là: {tich1}      
    Tích các số chia hết cho 3 nhỏ hơn hay bằng {n} là: {tich2}
    Tổng các số nguyên tố nhỏ hơn hay bằng {n} là: {tong3}       
    Tổng chuỗi đan dấu là: {round(tong4,2)}"""


# Tong n so nguyen nhap vao.
def tong_n_so_nguyen(n):
    i = 1
    tong = 0
    while i <= n:
        so = int(input(f"Nhap so thu {i} la: "))
        i += 1
        tong += so
    return f"tong {n} so nguyen vua nhap la:", tong


# Tinh tong cac so nguyen nhap vao va dung lai khi nhap 0.
def tinh_so_nguyen():
    flat = True
    i = 1
    tong = 0
    while flat == True:
        so = int(input(f"So thu {i} la: "))
        tong += so
        if so == 0:
            break
    return "tong cac so nhap vao la:", tong


# Tim UCLN cua a va b.
def ucln(a, b):
    while b:
        a, b = b, a % b
    return a


# Tim BCNN cua a,b.
def bcnn(a, b):
    kq = (a * b) / ucln(a, b)
    return kq


# Tim BCLN cua a,b.
def bcln(a, b):
    kq = (a * b) / bcnn(a, b)
    return kq


# Tim so hoan hao.
def so_hoan_hao(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    if tong == n:
        return "Day la so hoan hao"
    else:
        return "Day khong la so hoan hao"


# Dao nguoc so.
def dao_nguoc_so(value):
    lst = []
    for i in value:
        if i != " ":
            lst.append(i)
    lst.reverse()
    for i in lst:
        if int(i) % 2 != 0:
            print(i, end=" ")
