import csv
from xu_ly_tap_tin_csv import *


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
