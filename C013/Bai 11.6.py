from Bai_tap_11.mo_ghi_tap_tin_csv import *

name_file = input("Nhập tên file: ")
list_write = []
list_write_big = []
name = input("Nhap ten: ")
fone = input("Nhap so dien thoat: ")
list_write.append(name)
list_write.append(fone)
list_write_big.append(list_write)

print(ghi_file_csv(name_file, list_write_big))
print(read_file(name_file))
