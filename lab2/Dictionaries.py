#упорядоченная*, изменяемая и не допускающая дубликатов коллекция.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#элементы словаря Access
y = thisdict.get("model")
    #keys()вернет список всех ключей в словаре
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
t = car.keys()
print(t) #before the change
car["color"] = "white"
print(t) #after the change
#Изменить элементы словаря
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict1.update({"year": 2020})
#удаление элементов словарz
thisdict1.pop("model")        #pop()удаляет элемент с указанным именем ключа:
thisdict.popitem()        #popitem()удаляет последний вставленный элемент
del thisdict["model"]        #delслово удаляет элемент с указанным именем ключа
#Циклические словари
for x in thisdict:
  print(thisdict[x])
#same
for x in thisdict.values():
  print(x)
for x, y in thisdict.items():   #Переберите ключи и значения
  print(x, y)
#Копирование словарей
    #copy() and dict()
mydict = dict(thisdict)
print(mydict)
#вложенные словари
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
clear()	#Removes all the elements from the dictionary
copy()	#Returns a copy of the dictionary
fromkeys()	#Returns a dictionary with the specified keys and value
get()	#Returns the value of the specified key
items()	#Returns a list containing a tuple for each key value pair
keys()	#Returns a list containing the dictionary's keys
pop()	#Removes the element with the specified key
popitem()	#Removes the last inserted key-value pair
setdefault()	#Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	#Updates the dictionary with the specified key-value pairs
values()	#Returns a list of all the values in the dictionary