#1
import math
v=int(input("Input degree: "))
res=v*math.pi/180
print("Output radian: ", res)
#2
height=int(input("Height: "))
first_value=int(input("Base, first value: "))
second_value=int(input("Base, second value: "))
area=0.5*height*(first_value+second_value)
print("Expected Output: ", area)
#3
num=int(input("Input number of sides: "))
leght=int(input("Input the length of a side: "))
polygon=(num*leght**2)/(4*math.tan(math.pi/num))
print("The area of the polygon is: ", polygon)
#4
b=int(input("Length of base: "))
h=int(input("Height of parallelogram: "))
par=b*h
print("Expected Output: ", par)
