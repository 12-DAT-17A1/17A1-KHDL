lst = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71]
lst1 = []
for i in lst:
    inch = i * 0.0254
    lst1.append(round(inch, 4))
print("Ba chiều cao đầu tiên:", lst1[0:3])
print("Ba chiều cao cuối cùng:", lst1[-3:])
print("Chiều cao trung bình:", round(sum(lst1) / len(lst1), 4))
print("Chiều cao lớn nhất:", max(lst1))
print("Chiều cao nhỏ nhất:", min(lst1))
lst1.sort()
print("Sắp xếp list theo thứ tự tăng dần:", lst1)
lst1.reverse()
print("Sắp xếp list theo thứ tự giảm dần:", lst1)
