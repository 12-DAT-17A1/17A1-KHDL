print("KIỂM TRA DỮ LIỆU ZIP CODE VIỆT NAM")
print("Mã zip hợp lệ bao gồm 6 chữ số")
n = input("Nhập mã zip: ")


def ktr_ma_zip(n):
    if len(n) == 6:
        if n.isdigit():
            return True
        else:
            return False
    else:
        return False


print(ktr_ma_zip(n))
