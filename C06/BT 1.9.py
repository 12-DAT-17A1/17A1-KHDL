#Bai 1.9:
tien_gui = float(input("Số tiền gửi: "))
thang_gui = float(input("Số tháng gửi: "))
lai_xuat = float(input("Lãi xuất một năm (%): "))
tien_lai = (tien_gui*thang_gui)*(lai_xuat/100/12)
von_lai = tien_gui + tien_lai
print("Tiền lãi =",tien_lai)
print(f"Tiền vốn + lãi = {tien_gui} + {tien_lai} = {von_lai}")







