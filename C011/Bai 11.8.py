def lucky_number(lst):
    for i in lst:
        if i % 7 == 0:
            return True
    else:
        return False


print(
    "Nhập một danh sách được xem là"
    + " may mắn"
    + " nếu có ít nhất một số chia hết cho 7 ☠"
)
print(
    """Nếu kết quả là True ==> lucky number
Nếu kết là False ==> không phải lucky number"""
)
print("Nhập các phần tử vào danh sách giữa các số là dấu cách⚠⚠⚠:")
lst = eval(input("nums = "))
print("Kết quả là:", lucky_number(lst))
