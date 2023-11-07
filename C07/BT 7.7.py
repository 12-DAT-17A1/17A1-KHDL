a = int(input("Số tiền muốn đổi là: "))
s1 = a // 500000
x1 = a % 500000
print("Số tờ 500,000 là: ", s1  )
s2 = x1 //200000
x2 = x1 % 200000
print("Số tờ 200,000 là: ",s2)
s3 = x2 //100000
x3 = x2 % 100000
print("Số tờ 100,000 là: ",s3)
s4 = x3 //50000
x4 = x3 % 50000
print("Số tờ 50,000 là: ",s4)
print("Tiền còn lại là: ",x4)














