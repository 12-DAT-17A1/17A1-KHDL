print("TÍNH TỔNG SỐ NGUYÊN NHẬP VÀO, CHẤM DỨT KHI NHẬP SỐ 0:")
sum = 0

a = 1
while (a > 0) : 
    x = eval(input("Nhập một số nguyên(kết thúc là số 0): ")) 
    if x==0:
       break
    sum+=x
print(f"Tổng số nguyên nhập vào(kết thúc là số 0) là: ",sum)

