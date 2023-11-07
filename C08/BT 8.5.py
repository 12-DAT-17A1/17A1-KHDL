print("KIỂM TRA NĂM NHUẬN")
nam = int(input("Năm nhập vào đây: "))
if (nam % 4 == 0 and nam % 100 != 0) or (nam%400==0):
    print(f"NĂM {nam} LÀ NĂM NHUẬN ")
else :
    print(f"NĂM {nam} KHÔNG PHẢI LÀ NĂM NHUẬN")    