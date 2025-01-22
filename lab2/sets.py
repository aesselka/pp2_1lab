# неупорядоченная , неизменяемая* и неиндексированная коллекция 
thisset = {"apple", "banana", "cherry"}
print(thisset)
#Доступ к элементам набора
thisset1 = {"apple", "banana", "cherry"}
print("banana" in thisset1) #true
#Добавить элементы набора
    #update() добавить элементы из другого набора в текущий набор на рандом
thisset3 = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset3.update(tropical)
print(thisset3)
#Удалить элементы набора
    #удалить элемент из набора, используйте метод remove(), или discard()
    #случайный элемент, используя pop()
    #clear() очищает весь набор
thisset4 = {"apple", "banana", "cherry"}
thisset4.discard("banana")
print(thisset4)
#наборы циклов
thisset5 = {"apple", "banana", "cherry"}
for x in thisset5:
  print(x)
#Объединение наборов
'''Методы union()и update()объединяют все элементы из обоих наборов.
Метод intersection()сохраняет ТОЛЬКО дубликаты.
Метод difference()сохраняет элементы из первого набора, которых нет в другом наборе(ах).
Метод symmetric_difference()сохраняет все элементы, КРОМЕ дубликатов.'''
a = {1, 2, 3, 4, 5}
b = {2, 4, 6, 8, 10}
print(a.add(b))                            # Adds element b to set a
print(a.clear())                           # Removes all elements from set a
print(a.copy())                            # Returns a copy of set a
print(a.difference(b))                     # Returns a set with elements in a but not in b
print(a.difference_update(b))              # Removes elements in b from set a
print(a.discard(b))                        # Removes element b from set a if it exists
print(a.intersection(b))                   # Returns a set with elements common to a and b
print(a.intersection_update(b))            # Keeps only elements in both a and b
print(a.isdisjoint(b))                     # Returns True if a and b have no elements in common
print(a.issubset(b))                       # Returns True if all elements of a are in b
print(a < b)                               # Checks if a is a proper subset of b
print(a.issuperset(b))                     # Returns True if all elements of b are in a
print(a > b)                               # Checks if a is a proper superset of b
print(a.pop())                             # Removes and returns an arbitrary element from a
print(a.remove(b))                         # Removes element b from a, raises KeyError if b is not in a
print(a.symmetric_difference(b))           # Returns a set with elements in either a or b but not both
print(a.symmetric_difference_update(b))    # Updates a with elements in either a or b but not both
print(a.union(b))                          # Returns a set with all elements from a and b
print(a.update(b))                         # Adds elements from b to a