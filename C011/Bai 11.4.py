from functools import reduce


def ktr(lst):
    for i in lst:
        if i >= 5:
            return False  # 5 ko phải là số lớn nhất
    return True


lst = []
lst1 = []
lst2 = []
spt = int(input("Số phần tử trong list: "))
check = int(input("Nhập giá trị cần tìm:"))
for i in range(1, spt + 1):
    nhap = int(input(f"Nhập giá trị thứ {i}: "))
    lst.append(nhap)
print("List:", lst)
# Tính tổng các phần tử trong list.(function reduce, lambda)😁
list_sum = reduce(lambda x, y: x + y, lst)
print("Tổng các phần tử trong list là:", list_sum)
dem = lst.count(check)
print(f"{check} xuất hiên {dem} lần trong list")
if ktr(lst):
    print("5 lớn hơn tất các số trong list")
else:
    print("5 không lớn hơn tất cả các số trong list")
for k in lst:
    if k > 5:
        lst2.append(k)
my_list = list(set(lst2))
print("Các số lớn hơn 5 trong list:", my_list)
