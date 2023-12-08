from functools import reduce
from operator import add


def snt(x):
    if x > 1:
        for i in range(2, x):
            if x % i == 0:
                return False  # Không phải só nguyên tố
            else:
                return (
                    True  # x là số nguyên tố vì x không là bội số của số nào từ 2 đến x
                )

    else:
        return False


def tong_list(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum


lst, lst1, lst2, lst3, lst4, lst5 = [], [], [], [], [], []
print("Lưu ý: Giữa các số phải có dấu cách ⚠")
select = input("Nhập số phần tử trong list: ").split()
for i in select:
    lst.append(int(i))
print(lst)
# Liệt kê các phần tử là số nguyên tố trong list.🤔
for j in lst:
    lst1.append(j)
for h in lst1:
    if snt(h):
        lst3.append(h)
ht = set(lst3)  # Loại bỏ các phần tử giống nhau
print("Các só nguyên tố trong list là:", list(ht))
# Liệt kê các phần tử âm trong list.
for negative in lst:
    if negative < 0:
        lst2.append(negative)
        lst4.append(negative)
    else:
        lst5.append(negative)
print("Các phần tử âm trong list là:", lst2)
# Tính trung bình cộng của các phần tử âm.😒
print("Trung bình cộng các số âm trong list là:", round(tong_list(lst4) / len(lst4), 2))
# Liệt kê các phần tử dương trong list.
print("Các phần tử dương trong list là:", lst5)
# Tính trung bình cộng của các phần tử dương (function: reduce , add) 😁
sum_list = reduce(add, lst5)
print("Trung bình cộng các số dương trong list:", round(sum_list / len(lst5), 2))
# Tìm gtln và gtnn😂
print("Giá trị lớn nhất trong list là:", max(lst))
print("Giá trị nhỏ nhât trong list là:", min(lst))
# sắp xếp theo thứ tự tăng dần.😒
lst.sort()
print("Xắp xếp các phần tử theo thứ tăng dần:", lst)
