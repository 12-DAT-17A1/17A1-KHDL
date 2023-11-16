print("VIẾT HÀM KIỂM TRA MỘT SỐ CÓ PHẢI LÀ SỐ HOÀN HẢO")
def so_hoan_hao(x):
    dem = 0
    for i in range(1,x):
       if x%i==0:
         dem+=i
    if dem==x:
        return "Đây là số hoàn hảo" 
    else:
        return "Đây không là số hoàn hảo" 
n = int(input("Nhập số để kiểm tra: "))
print(so_hoan_hao(n))