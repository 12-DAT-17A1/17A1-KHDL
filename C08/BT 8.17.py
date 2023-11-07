def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

# Nhập hai số nguyên từ bàn phím
num1 = int(input("Nhập số nguyên thứ nhất: "))
num2 = int(input("Nhập số nguyên thứ hai: "))

# Tính và in kết quả LCM
result = lcm(num1, num2)
print("Bội chung lớn nhất của", num1, "và", num2, "là:", result)
