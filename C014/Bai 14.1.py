try:
    a = int(input("Nhap canh a: "))
    b = int(input("Nhap canh b: "))
    c = int(input("Nhap canh c: "))
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Lỗi do có giá trị nhập vào âm hoặc bằng không!!!")
    if (a + b <= c) or (a + c <= b) or (c + b <= a):
        raise ValueError("Lỗi vì ba cạnh nhập vào khồng tạo thành tam giác!!!")
except ValueError as er:
    print("Lỗi:", er)
