print("Tính năm âm lịch từ năm dương lịch.")
def duong_to_am(nam):
    can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "ẤT", "Bính", "Đinh", "Mậu", "Kỷ"]
    chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý","Sửu","Dần", "Mão", "Thìn","Tỵ", "Ngọ", "Mùi" ]
    can_index = nam % 10
    chi_index = nam % 12
    nam_am =  f"{can[can_index]} {chi[chi_index] }"     
    return nam_am
# Sử dụng hàm để chuyển đổi từ năm dương lịch 2023 sang năm âm lịch
nam_duong = int(input("Nhập năm: "))
nam_am = duong_to_am(nam_duong)
print(f"Năm âm lịch tương ứng với {nam_duong} là {nam_am}")

 





























