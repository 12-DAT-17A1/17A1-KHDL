def compase(a, lst1):
    lst = []
    for i in lst1:
        if a >= i:
            lst.append(False)
        else:
            lst.append(True)
    return lst


print("Lưu ý: Nhập trên 1 dòng giữa các phần tử nhập vào cách nhau một dấu cách⚠")
lst = eval(input("Nhập danh sách của bạn:"))
number = int(input("thresh = "))
print(compase(number, lst))
