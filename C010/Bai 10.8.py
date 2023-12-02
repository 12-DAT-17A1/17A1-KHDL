print("SD HÀM DATETIMES")
from time import *
from datetime import *
import calendar


a = int(input("Nhập ngày: "))
b = int(input("Nhập tháng: "))
c = int(input("Nhập năm: "))


def tinh_nam_nhuan(x):
    a = calendar.isleap(c)
    if a == True:
        return f"Năm {x} là năm nhuận"
    else:
        return f"Năm {x} không là năm nhuận"


ngay_hien_tai = datetime(c, b, a)
ngay_thang_nam = ngay_hien_tai.strftime("%d-%m-%Y")
print("Ngày tháng năm vừa nhập: ", ngay_thang_nam)
print(tinh_nam_nhuan(c))
print(f"{ngay_thang_nam} là Thứ", calendar.weekday(c, b, a) + 2)
ngay = calendar.monthrange(c, b)
for i in ngay:
    if i <= 8:
        continue
    else:
        print(f"Số ngày trong tháng {b} là:", i)
