tp1 = eval(input("Nhập Tuple a: "))
tp2 = eval(input("Nhập Tuple b: "))
tp3 = tp1 + tp2
print("Tuple c:", tp3)
lst = []
for i in tp3:
    lst.append(i)
lst.sort()
tp4 = tuple(lst)
print("Tuple d:", tp4)
print("Phần tử thứ 3 của Tuple là:", tp4[2])
print("Ba phần tử cuối cùng của tuple d là:", tp4[-3:])
