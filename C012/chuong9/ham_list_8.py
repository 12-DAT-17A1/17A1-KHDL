# Tìm só lớn nhất và số nhỏ nhất của 4 số nhập vào.
def find_max_min(a, b, c, d):
    lst = [a, b, c, d]
    return f"Max là: {max(lst)}\nMin là: {min(lst)}"


# Chương trình count down.
def count_down(so):
    lst = []
    for i in range(so, 0, -1):
        lst.append(i)
    for j in lst:
        print(j)
    print("Start!!!")


# Tìm đội trưởng của đội tồi tệ nhất.
def tim_doi_truong(team_number):
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
