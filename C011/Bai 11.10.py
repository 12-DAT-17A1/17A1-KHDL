def menu_is_boring(meals):
    st = set(meals)
    if len(meals) > len(st):
        return True
    return False


print("Kq là: True ==> Bữa ăn nhàm chán.\n" "Kq là: False ==> Bữa ko nhàm chán.")

menu = eval(input("Nhập list Menu❓: "))
print(menu_is_boring(menu))
