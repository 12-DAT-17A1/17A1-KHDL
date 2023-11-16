print("Tính biểu thức A = (x^2 + x +1)^n  + (x^2 - x +1)^n")
def A(n,x):
    return (x**2 + x +1)**n  + (x**2 - x +1)**n
n = int(input("Nhập n: "))
x = int(input("Nhập x: "))
print(A(n,x))























