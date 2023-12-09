n = int(input("Nhập số lượng con thú: "))
m = input("Con thú cần tìm là: ")


def find(m, lst):  # Hàm tìm chuỗi trong một list.😒
    find = m in lst
    if find == True:
        return True
    return False


lst = []
for i in range(n):
    name_animal = input("name animal: ")
    lst.append(name_animal)  # Thêm phần tử vào lst🤷‍♂️
print("List of animals:", lst)
print("I want to find:", m)
if find(m, lst):
    print(f"there is {m} in list of animals")
else:
    print(f"There is no {m} in the list of animals")
