import math

def approximate_exponential(x, tolerance):
    result = 1.0  # Khởi tạo giá trị ban đầu cho chuỗi
    term = 1.0    # Giá trị của thành phần hiện tại
    n = 1         # Biến đếm

    while abs(term) >= tolerance:
        term *= x / n
        result += term
        n += 1

    return result

# Nhập giá trị x từ người dùng
x = float(input("Nhập giá trị x: "))
tolerance = 1e-4  # Sai số cần thiết

approximated_value = approximate_exponential(x, tolerance)
exact_value = math.exp(x)

print(f"Giá trị gần đúng của e^{x}: {approximated_value}")
print(f"Giá trị chính xác của e^{x}: {exact_value}")
