# class House():
#     '''описание дома '''
#     def __init__(self, street, num):
#         self.street = street
#         self.num = num
#         self.age=0
#     def build(self):
#         '''строит дом'''
#         print("Dom na ulice" + self.street +" pod num "+ str(self.num) )
#     def ageofhouse(self,year):
#         self.age+=year

# House1= House(" Алматинка", 21)
# House2= House(" Moskva",22)
# House1.build()
# House1.ageofhouse(5)
# print(House1.age) 
#1
import math
class Myhouse():
    def __init__(self):
        self.numofhouse=""
    def getString(self):0
    self.numofhouse=input("write a что то: ")
    def printtString(self):
        print(self.numofhouse.upper())
House= Myhouse()
House.getString()
House.printtString()
#2
class Shape():
    def __init__(self):
        self.dfarea=0
class Square(Shape):
    def __init__(self,dlinna):
        super().__init__()
        self.dlinna=dlinna
    def area(self):    
        return self.dlinna*self.dlinna
Sq=Square(5)
print(Sq.area())
#3
class Rectangle(Shape):
    def __init__(self,length,width):
        self.lenght=length
        self.width=width
    def area(self):
        return self.lenght*self.width
Rt=Rectangle(4,5)
print(Rt.area())
#4
class Point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print("точки координат:" + str(self.x)+" "+ str(self.y))
    def move(self,new_x,new_y):
        self.x=new_x
        self.y=new_y
    def dist(self,oth):
        return math.sqrt((self.x-oth.x)**2+(self.y-oth.y)**2)
Po1=Point(2,3)
Po2=Point(5,7)
Po1.show()
Po1.move(3,5)
print(Po1.dist(Po2))
#5
class Bank():
    def __init__(self,owner,balance=0):
        self.balance=balance
        self.owner=owner
    def deposit(self,amount):
        self.balance+=amount
        print("Новый баланс:"+ str(self.balance))
    def withdraw(self,amount):
        if amount >self.balance:
            print("не хватает")
        else:
            self.balance-=amount
            print("Cнятие "+ str(amount)+" New balance: "+ str(self.balance))
acc=Bank("Assel", 1000)
acc.deposit(500)
acc.withdraw(300)
#6
def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%2==0:
            return False
        return True
lyst=[1,2,3,4,5,6,7,8,9,10,11]
print(list(filter(lambda num: prime(num) , lyst)))
