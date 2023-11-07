print("TÍNH TỔNG N SỐ NGUYÊN NHẬP VÀO:")
n = int(input("N ="))
sum = 0
for i in range(1,n+1):
    a = eval(input(f"Nhập số nguyên thứ {i}: "))
    if a==n:
        break
    sum+=a
print(f"Tổng của {n} số nguyên nhập vào là: ",sum)









