#1
import math
lst=[1,25,3,49]
nu=list(map(lambda x : pow(x,2),lst))
print(sum(nu))
#2
a=input()
upp=sum(map(str.isupper, a))
loww=sum(map(str.islower, a))
print(upp+loww)
#3
b=input()
nin=b.lower()
if b==nin[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")
#4
import time
num=int(input())
tme=int(input("time:"))
tme2=time.sleep(tme/1000)
srt=math.sqrt(num)
print(f"Square root of {num} after {tme} miliseconds is {srt}")
#5
my_tuple = (1, True, 'idccd', [1, 2, 3])
res = all(my_tuple)
print(res)  