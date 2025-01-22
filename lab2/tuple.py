tuple1 = ("abc", 34, True, 40, "male")
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple this will be string
thistuple1 = ("apple")
print(type(thistuple1))
#доступ к элементам кортежа
thistuple2  = ("apple", "banana", "cherry")
print(thistuple2[1])
# Обновление кортежей
thistuple3 = ("apple", "banana", "cherry")
y = list(thistuple3)
y.remove("apple")
thistuple3 = tuple(y)
#распаковка кортежей
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)
#Циклические кортеж
thistuple4 = ("apple", "banana", "cherry")
for i in range(len(thistuple4)):
  print(thistuple4[i])
#Объединение кортежей
ruits = ("apple", "banana", "cherry")
mytuple = ruits * 2
print(mytuple)
#Методы кортежа
thistuple5 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
c = thistuple5.count(5)
print(c)
#