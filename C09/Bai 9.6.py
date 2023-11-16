print("HÀM KIỂM TRA X CÓ LÀ SỐ NGUYÊN TỐ HAY KHÔNG.")
def ham_kiem_tra_so_nguyen_to(x):
 if x> 1:
    for i in range(2,x):
        if x%i==0:
         return False 
    return True
 else:
        return False
n = int(input("Nhập số: "))
print(ham_kiem_tra_so_nguyen_to(n))

