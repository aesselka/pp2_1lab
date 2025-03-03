import os

#task 1
def list_content(path):
    all_items = os.listdir(path)

    print(os.path.isdir(os.path.join(path)))

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("all items: ", all_items)
    print("directories: ", directories)
    print("files: ", files)

path = "."
list_content(path)

#task 2
print('Exist:', os.access(path, os.F_OK))
print('Readable:', os.access(path, os.R_OK))
print('Writable:', os.access(path, os.W_OK))
print('Executable:', os.access(path, os.X_OK))
#task 3
path = '/Users/aesselka/Desktop/VSCODE'
if os.access(path, os.F_OK):
    filename = os.path.basename(path)
    print(filename)
else:
    print('Exist:', os.access(path, os.F_OK))
#task 4
cnt = 0
with open('лаб6/A.txt', 'r', encoding='utf-8') as f:
    for _ in f:
        cnt+=1

print(cnt)

#task 5
lst = [1,2,3,4,5,6,7,8]
with open('newfile.txt', 'w') as f:
    for i in lst:
        f.write(str(i) + '\n')

#task 6
import os
os.makedirs('txts', exist_ok=True)
for i in range(65, 91):
    s = chr(i)
    file_path = f"лаб6/{s}.txt"

    try:
        with open(file_path, 'x') as f:
            print(f"file {file_path} created!")
    except FileExistsError:
        print(f"File {file_path} already exists!")

#task 7
with open('лаб6/A.txt', 'r') as rd, open('newfile.txt', 'w') as wt:
    wt.write(rd.read())


#task 8
df = 'лаб6/text.txt'
if os.path.exists(df):
    if os.access(df, os.F_OK):
        os.remove(df)
    else:
        print("Permision denied")
else:
    print("does not exist")