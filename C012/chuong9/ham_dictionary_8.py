# Tính cước taxi.
# Tính cước taxi cho xe 4 chỗ và 7 chỗ với giá mỗi km
def tinh_cuoc_taxi(loai_xe, khoang_cach, thoi_gian_cho):
    thong_tin_cuoc = {
        "4": {
            "cuoc_codinh": 5,
            "don_gia_khoang_cach": 2.5,
            "don_gia_thoi_gian_cho": 0.5,
            "gia_moi_km": 1.2,
        },
        "7": {
            "cuoc_codinh": 7,
            "don_gia_khoang_cach": 3,
            "don_gia_thoi_gian_cho": 0.6,
            "gia_moi_km": 1.5,
        },
    }

    if loai_xe in thong_tin_cuoc:
        cuoc = (
            thong_tin_cuoc[loai_xe]["cuoc_codinh"]
            + thong_tin_cuoc[loai_xe]["don_gia_khoang_cach"] * khoang_cach
            + thong_tin_cuoc[loai_xe]["don_gia_thoi_gian_cho"] * thoi_gian_cho
            + thong_tin_cuoc[loai_xe]["gia_moi_km"] * khoang_cach
        )
        return cuoc
    else:
        return "Không có thông tin cước cho loại xe này"


# Tính tiền thuê phòng resort.
def tien_resort(loai_phong, so_dem):
    thong_tin = {
        "1": 1260000,
        "2": 1550000,
        "3": 1830000,
        "4": 1830000,
        "5": 2120000,
        "6": 2120000,
        "7": 2540000,
        "8": 4480000,
    }
    if 2 <= so_dem <= 3:
        tien = (thong_tin[loai_phong] - (thong_tin[loai_phong] * 0.3)) * so_dem
        return "Số tiền phải trả là: {:,}".format(tien)

    else:
        tien = (thong_tin[loai_phong] - (thong_tin[loai_phong] * 0.3)) * so_dem
        return "Số tiền phải trả là: {:,}".format(tien)
