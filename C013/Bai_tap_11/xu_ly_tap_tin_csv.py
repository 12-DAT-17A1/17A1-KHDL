import csv


def read_file_csv(name_file):
    with open(name_file, "r") as file_read:
        for i in csv.reader(file_read):
            print(i)
