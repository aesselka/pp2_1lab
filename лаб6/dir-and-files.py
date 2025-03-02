import os
#task 1
def list_content(path):
    all_items = os.listdir(path)

    print(os.path.exists(path))

    directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
    files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

    print("all its: ", all_items)
    print("dirs: ", directories)
    print("files: ", files)

path = "."
list_content(path)
#task2
str = "hrlli vorld"
appr = 0
lowr = 0
for i in str:
    if i.isupper():
        appr += 1
    elif i.islower and i != " ":
        lowr += 1

print(appr, lowr)
#task3
def is_palindrome(strr):
    strr = strr.replace(" ", "").lower()
    if str == str[::-1]:
        print(f'"{strr}" palindrome.')
        return
    else:
        print(f'"{strr}" not palindrome.')
        return

str1 = "lvl"
is_palindrome(str1)

str2 = "bye"
is_palindrome(str2)
#task
import time

chislo = 25100
zaderzhka = 2123

time.sleep(zaderzhka / 1000)  

res = chislo ** 0.5

print(f"Square root of {chislo} after {zaderzhka} milliseconds is {res}")

#task
def isTrue(tup):
    return all(tup)

tup1 = (True, True, True)
tup2 = (True, False, True)

print(isTrue(tup1))
print(isTrue(tup2))