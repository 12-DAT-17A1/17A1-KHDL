print("NHẬP SỐ ĐIỆN ĐỂ TÍNH TIỀN ĐIỆN:")
s = int(input("Nhập số điện (kWh): "))
if s>=0 and s<=50:
    print("TIỀN ĐIỆN LÀ: {}".format(s*1678),"đồng")
elif s>50 and s<=100:    
    S = s*1734
    print(f"TIỀN ĐIỆN LÀ: {S}","đồng")
elif s>100 and s<=200:     
    print("TIỀN ĐIỆN LÀ:",s*2014,"đồng")
elif s>200 and s<=300:     
    print("TIỀN ĐIỆN LÀ:",s*2536,"đồng")
elif s>300 and s<=400: 
    print("TIỀN ĐIỆN LÀ:",s*2834,"đồng")   
else:
    print("TIỀN ĐIỆN LÀ:",s*2927,"đồng")   
    
   
    