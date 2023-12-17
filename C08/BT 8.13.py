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


def snt(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    tong = 0
    for i in range(2, n + 1):
        if snt(i):
            tong += i
    print(f"Tổng các số nguyên tố nhỏ hơn hay bằng {n} là:", tong - 2)
sum2 = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        i = -1 / i
    else:
        i = 1 / i
    sum2 += i
print("Tổng chuỗi đan dấu là: ", round(sum2, 2))
