# Đọc nội dung file.
def read_file(name_file):
    f = open(name_file + ".txt", "r")
    content = f.read()  # Đọc toàn bộ nội dung trong file.
    return content


# Đọc nội dung file và các thông tin cơ bản khác.
def read_report_file(name_file):
    with open(name_file + ".txt", "r") as f:
        a = f.read()  # Đọc tất cả nội dung trong file.
        content = f"Nội dung tập tin:\n{a}"
        f.seek(0)  # Con trỏ về đầu tập tin.
        counts = 0
        b = f.read()
        for i in b:
            if i.isalpha():  # Trả true nếu nếu i là ký tự và ngược lại False.
                counts += 1

        f.seek(0)  # Con trỏ về đầu tập tin: 0; từ vị trí hiện tại: 1; cuối tập tin: 2.
        counts_chain = 0
        c = f.read()
        chain = c.split()
        for i in chain:
            counts_chain += 1
        print(content)
        print("Số từ là:", counts_chain)
        print("Số ký tự là:", counts)


# Tạo-ghi-đọc:file.
def write_file(name_file, content):
    with open(name_file, "w", encoding="utf-8") as f:
        f.write(content)  # Tạo nội dung trong file.
    with open(name_file, "r") as f:
        read_file = f.read()  # Đọc toàn bộ nội dung trong file.
    return read_file


# Tao-ghi-đọc-chèn: file.
def write_end_of_file(name_file):
    with open(name_file, "a+") as f:
        chain = input("Nhập nội dung: ")
        f.write(f"{chain}\n")
        f.readline()
        so = int(
            input("Bạn có muốn tiếp tục ghi nội dung vào file không(1: có; 0: không): ")
        )
        while so == 1:
            f.readline()
            chain_new = input("Nhập nội dung: ")
            f.write(f"{chain_new}\n")
            so = int(
                input(
                    "Bạn có muốn tiếp tục ghi nội dung vào file không(1: có; 0: không): "
                )
            )
    with open(name_file, "r") as f:
        read_file = f.read()
        return read_file
