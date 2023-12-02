print("SD HÀM MAX, MIN")
n = int(input("Số giá trị nhập vào là: "))
lst = []
i = 0
for i in range(n):
    i += 1
    i = int(input(f"Số thứ {i} là: "))
    lst.append(i)
print("GIÁ TRỊ LỚN NHẤT LÀ:", max(lst))
print("GIÁ TRỊ NHỎ NHẤT LÀ:", min(lst))
