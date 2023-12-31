def ktr_chuoi(number):
    if isinstance(number, str):
        raise ValueError("Lỗi do nhập chuỗi")


def ktr_count(number):
    chain = str(number)
    for i in chain:
        counts = chain.count(i)
        if counts >= 4:
            raise ValueError("Lỗi vì có số bị nhập lại 4 lần!!!")


number = 1
while number != 0:
    try:
        number = int(input("Mời nhâp số nguyên dương: "))
        ktr_chuoi(number)
        ktr_count(number)
        if number < 0:
            raise ValueError("Lỗi do người dùng nhập vào số âm!!!")
    except ValueError as er:
        print(er)
