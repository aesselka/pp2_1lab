import re
#1
row=["abb","abs","asb","a0b","atb","abbbb","ab","abbb"]
for i in row:
    if re.fullmatch(r'ab*', i):
        print(str(i),"is correct")
    else:
        print(str(i),"is not correct")
#2
for i in row:
    if re.fullmatch(r'ab{2,3}$',i):
        print(str(i),"is correct")
    else:
        print(str(i),"is not correct")
#3
text3=["apple_tree is growing fast in garden under_the_sky"]
for i in text3:
    m=re.findall(r'\b[a-z]+(?:_[a-z]+)+\b',i)
    for j in m:
        print(j)
#4

