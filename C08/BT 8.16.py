def UCLN(a, b):
    while b:
        a, b = b, a % b
    return a

# Nhập hai số nguyên từ bàn phím
num1 = int(input("Nhập số nguyên thứ nhất: "))
num2 = int(input("Nhập số nguyên thứ hai: "))

# Gọi hàm tính ước chung lớn nhất và in kết quả
result = UCLN(num1, num2)
print("Ước chung lớn nhất của", num1, "và", num2, "là:", result)



















