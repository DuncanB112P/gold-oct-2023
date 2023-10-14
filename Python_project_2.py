import os

File_Info = []

files = os.listdir()

for file in files:
    size = os.path.getsize(file)
    File_Info.append({file : size})

print(File_Info)