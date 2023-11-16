print("Tính chỉ số BMI:")
def BMI(can_nang,chieu_cao):
    bmi = (can_nang)/(chieu_cao)**2
    print("Chỉ số BMI là:%0.3f"%bmi)
    if bmi<18.5:
        return "Gầy"
    elif 18.5<bmi<24.99:
        return "Bình thường"
    else:
        return "Thừa cân"
a = eval(input("Nhập số cân nặng (kg): "))
b = eval(input("Nhập số chiều cao(m): "))
print("Dáng người là:",BMI(a,b))


















