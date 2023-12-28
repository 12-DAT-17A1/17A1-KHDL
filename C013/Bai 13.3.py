from Library import *

# Mở đọc ghi file.
name_file = input("Enter name file: ")
content = input("Enter content: ")
print("Content file:\n", write_file(name_file, content))
