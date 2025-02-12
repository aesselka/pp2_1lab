#List Items - Data Types
list1=["pen","pencil"]
print(type(list1))
mylist=list(("apple", "rabbit"))
print(mylist)
#Python - Access List Items
list2=["pen","apple","rabbit","pencil"]
print(list2[-2])
print(list[0])
print(list[1:3])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
#Python - Change List Items
thislist1 = ["dwsc", "wcdd", "cwdsc"]
thislist1[1] = "dcwdcr"
print(thislist1)
thislist2 = ["apple", "samsung", "huawei"]
thislist2.insert(2, "li9")# используем чтобы задать индекс по нему добавить элемент,
# а append просто добавлять в самом низу списка
print(thislist2)
# Добавить элементы списка 
thislist3 = ["apple", "samsung", "huawei"]
tropical = ["dwsc", "wcdd", "cwdsc"]
thislist3.extend(tropical)
print(thislist3)
#удаление элементов списка
#Метод remove()удаляет указанный элемент,более одного элемента с указанным значением, remove()метод удаляет первое
list4 = ["apple", "samsung", "huawei"]
list4.remove("apple")
print(list4)
list5=["pizza","sweets","burger"]
list5.pop(2)
print(list5)
thislist4 = ["apple", "banana", "cherry"]
del thislist4 # может удалить весь список
#thislist4.clear() #clear() очищает список но сохраняет выдает пустой
#Циклические списки
d=["pop","kitty","rare"]
for i in d:
  print(i)
h=0
while h<len(d):
  print(d[h])
  h+=1
#they are equal to each other
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)
#sort list
list1 = ["abc", 34, True, 40, "male"] #unlike arrays, lists may contain elements of various data types in the same time 
print(type(mylist))  #So the output is <class 'list'>, it is not an array
#copy list
thislists = ["apple", "banana", "cherry"]
mylists = thislists.copy()
print(mylists)
#join list
list7 = ["a", "b", "c"]
list8 = [1, 2, 3]
list9 = list7 + list8
print(list9)

