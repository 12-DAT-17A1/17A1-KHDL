print("TÍNH CƯỚC XE TAXI:")
loai_xe = int(input("Xe mấy chỗ ngồi(4 or 7): "))
km = eval(input("Số km: "))
tg = eval(input("Thời gian chờ (phút): "))
if loai_xe==4 or loai_xe==7:  
    if loai_xe == 4:
        if km <= 0.8:
            if tg<=5:
                print("Tiền chờ là: MIỄN PHÍ ")   
                print("tiền di chuyển:11000 ")
                print("Tiền cước: {} ".format((tg*800)+(11000*km)))      
            else:
                print("Tiền chờ là:",tg*800)   
                print("tiền di chuyển:11000 ")
                print("Tiền cước: {} ".format((tg*800)+(11000*km)))
        if km > 0.8 and km <= 20:
            if tg<=5:
                print("Tiền chờ là: MIỄN PHÍ ")   
                print("tiền di chuyển:12100 ")
                print("Tiền cước: {} ".format((tg*800)+(12100*km)))      
            else:
                print("Tiền chờ là:",tg*800)   
                print("tiền di chuyển:12100 ")
                print("Tiền cước: {} ".format((tg*800)+(12100*km)))
        if km > 20:
            if tg<=5:
                print("Tiền chờ là: MIỄN PHÍ ")   
                print("tiền di chuyển:10000 ")
                print("Tiền cước: {} ".format((tg*800)+(10000*km)))      
            else:
                print("Tiền chờ là:",tg*800)   
                print("tiền di chuyển:10000 ")
                print("Tiền cước: {} ".format((tg*800)+(10000*km)))
    if loai_xe == 7:
        if km <= 0.8:
            if tg<=5:
                print("Tiền chờ là: MIỄN PHÍ ")   
                print("tiền di chuyển:13000 ")
                print("Tiền cước: {} ".format((tg*800)+(13000*km)))      
            else:
                print("Tiền chờ là:",tg*800)   
                print("tiền di chuyển:13000 ")
                print("Tiền cước: {} ".format((tg*800)+(13000*km)))
    if km > 0.8 and km <= 20:
        if tg<=5:
            print("Tiền chờ là: MIỄN PHÍ ")   
            print("tiền di chuyển:14100 ")
            print("Tiền cước: {} ".format((tg*800)+(14100*km)))      
        else:
            print("Tiền chờ là:",tg*800)   
            print("tiền di chuyển:14100 ")
            print("Tiền cước: {} ".format((tg*800)+(14100*km)))
    if km > 20:
        if tg<=5:
            print("Tiền chờ là: MIỄN PHÍ ")   
            print("tiền di chuyển:12000 ")
            print("Tiền cước: {} ".format((tg*800)+(12000*km)))      
        else:
            print("Tiền chờ là:",tg*800)   
            print("tiền di chuyển:12000 ")
            print("Tiền cước: {} ".format((tg*800)+(12000*km)))
                
       