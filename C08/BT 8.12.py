print("KIỂM TRA SỐ NGUYÊN TÓ:")
n = int(input("Nhập số: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Đây không là số nguyên tố")
            break
        else:
            print("Đây là số nguyên tố")
            break
else:
    print("Đây không là số nguyên tố")
