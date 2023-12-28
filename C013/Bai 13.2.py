from Library import *


print(
    """
Danh sách: 
1, dongchi
2, taytien
3, sangthu"""
)
chain = input("Nhập tên file: ")
print(read_report_file(chain))
