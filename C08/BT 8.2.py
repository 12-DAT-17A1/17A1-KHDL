from math import abs

print("TÌM TRỊ TUYỆT ĐỐI CỦA SỐ a")
try:
    a = eval(input("Nhập số a = "))
except:
    x = abs(a)
    print(x)
print(f"Trị tuyệt đối của {a} là:", x)
