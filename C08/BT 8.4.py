from math import*
print("TÍNH DIỆN TÍCH TAM GIÁC CÓ CÁC CẠNH LÀ A, B, C:")
A = eval(input("Cạnh A: "))
B = eval(input("Cạnh B: "))
C = eval(input("Cạnh C: "))
p = (A+B+C)/2
dien_tich = sqrt(p*(p-A)*(p-B)*(p-C))
print("DIỆN TÍCH TAM GIÁC LÀ: ",dien_tich)