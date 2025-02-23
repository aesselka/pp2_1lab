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
test1=["Anel,Dariya,Assel,bek,serdar,nurasyl"]
for i in test1:
    mk=re.findall(r'\b[A-Z]+[a-z]*',i )
    for j in mk:
        print(j)
#5
text1=["adcwsderb", "abdhcb","sdcb","ancrjt"]
for i in text1:
    if re.fullmatch(r'^a.*b$', i):
        print(str(i)+" is correct")
    else:
        print(str(i)+" is not correct")
#6
reg=r'[., ]+'
text2="После того как Анел закончила занятия в университете.она решила пойти в спортзал потому что почувствовала, что устала от сидячего"
replacement=':'
new=re.sub(reg, replacement, text2)
print(new)
#7
txt="This is a sample text with some patterns like first_name"
pattern = re.findall(r'[A-Za-z]+_[A-Za-z]+', txt)
cc = []
for i in pattern:
    a = i.split('_')
    cc.append(a[0]+''.join(x.capitalize() for x in a[1:]))
print(cc)
#8
text="JackDesk"
mkf=(re.sub(r'([a-z])([A-Z])', r'\1 \2', text))
print(mkf)
#9
pattern = re.sub(r'(?<!^)(?=[A-Z])', ' ', txt)
print(pattern)