print("TÍNH GIÁ TRỊ BIỂU THỨC:")
n = int(input("Nhập số: "))
sum = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        sum += i
print(f"Tổng các số lẻ nhỏ hơn hay bằng {n} là:", sum)
sum1 = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum1 += i
print(f"Tổng các số chẵn nhỏ hơn hay bằng {n} là:", sum1)
tich = 1
for i in range(1, n + 1):
    tich *= i
print(f"Tích các số từ 1 cho tới {n} là:", tich)
tich1 = 1
for i in range(1, n + 1):
    if i % 3 == 0:
        tich1 *= i
print(f"Tích các số chia hết cho 3 nhỏ hơn hay bằng {n} là:", tich1)
sum = 0
for i in range(n + 1):
    sum += 1
print(f"Tổng các số nguyên tố nhỏ hơn hay bằng {n} là:", sum)
sum2 = 0
for i in range(1, n + 1):
    i = 1 / i
    if i % 2 != 0:
        i = (0 - i) / (i + 1)
    sum2 += i
print("Tổng chuỗi đan dấu là: ", sum2)
