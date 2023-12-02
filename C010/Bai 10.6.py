from math import *


def giai_phuong_trinh_bac_hai(a, b, c):
    delta = b**2 - 4 * a * c
    if a != 0:
        if delta > 0:
            x1 = (-b + sqrt(delta)) / (2 * a)
            x2 = (-b - sqrt(delta)) / (2 * a)
            return f"PT có 2 nghiệm phân biệt là:\n x1 = {x1} \n x2 = {x2}"
        elif delta == 0:
            x = -b / (2 * a)
            return "PT có nghiệm kép là:\n x1 = x2 =", x
        else:
            return "PT vô nghiệm"
    else:
        return "Đây không là pương trình bậc hai"


# Phương trình ax^2 + bx + c = 0
a = eval(input("Nhập a: "))
b = eval(input("Nhập b: "))
c = eval(input("Nhập c: "))
print(giai_phuong_trinh_bac_hai(a, b, c))
