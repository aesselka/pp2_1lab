class CustomRange:
    def __init__(self,start,stop,step=1):
        self.start=start
        self.stop=stop
        self.step=step
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= self.stop:
                    break

        value = self.current
        self.current+=self.step
        return value
cr=CustomRange(2,10,2)
print(list(cr))
nums=[1,2,4,5,6,10]
pr=[]
for i in nums:
    if i>=0:
        pr.append(i)
    else:
        print("False")
if all(pr):
    print("True")

import math
a=int(input())
b=int(input())

def crs(a,b):
    return math.gcd(a,b)
print(crs(a,b))

