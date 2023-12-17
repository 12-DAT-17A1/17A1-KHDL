print("NHẬP SỐ ĐIỆN ĐỂ TÍNH TIỀN ĐIỆN:")
price1, price2, price3, price4, price5, price6 = 1678, 1734, 2014, 2536, 2834, 2927
s = int(input("Nhập số điện (kWh): "))
if s <= 50:
    coin = 50 * price1
elif s <= 100:
    coin = (50 * price1) + ((s - 50) * price2)
elif s <= 200:
    coin = (50 * price1) + (50 * price2) + ((s - 100) * price3)
elif s <= 300:
    coin = (50 * price1) + (50 * price2) + (100 * price3) + ((s - 200) * price4)
elif s <= 400:
    coin = (
        (50 * price1)
        + (50 * price2)
        + (100 * price3)
        + (200 * price4)
        + ((s - 300) * price5)
    )

else:
    coin = (
        (50 * price1)
        + (50 * price2)
        + (100 * price3)
        + (200 * price4)
        + (300 * price5)
        + ((s - 400) * price6)
    )
print("Số tiền cần nộp là: {:,}đ".format(coin))
