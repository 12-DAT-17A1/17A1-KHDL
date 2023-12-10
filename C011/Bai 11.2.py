team_number = int(input("Nhập số đội: "))
lst = []
for i in range(1, team_number + 1):
    lst1 = []
    nums = int(input(f"Số thành viên đội {i} là: "))
    for j in range(nums):
        select = input("Nhập tên thành viên: ")
        lst1.append(str(select))
    lst.append(lst1)
print(lst)
print("Tên đội trưởng của đội tồi tệ nhất là:", lst[-1][1])
