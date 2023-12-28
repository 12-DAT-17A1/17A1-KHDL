import csv


def write_csv_file(filename, listcontent):
    lst = []
    lst.append(listcontent)
    with open(filename, "a+", newline="") as file_new:
        for row in lst:
            csv.writer(file_new).writerow(row)


def read_file(file_name):
    with open(file_name, "r") as read_file:
        for row in csv.reader(read_file):
            print(row)


print(write_csv_file("file.csv", eval("[1,2,3,4,5]")))
print(read_file("file.csv"))


def ghi_file_csv(name_file, content):
    with open(name_file, "a+", newline="") as file:
        for i in content:
            csv.writer(file).writerow(i)


def read_file(filename):
    with open(filename, "r") as file_read:
        for row in csv.reader(file_read):
            print(row)
