from math import *

print(
    """
SD HÀM POW
TÍNH BIỂU THỨC: S = (x^2+x+1)^n+(x^2-x+1)^n """
)
x = eval(input("Nhập x: "))
n = eval(input("Nhập n: "))
bt = pow(pow(x, 2) + x + 1, n) + pow(pow(x, 2) - x + 1, n)
print("Kết quả là:", int(bt))
