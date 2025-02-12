a = '''
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])
c = "Hello, World!"
print(c[-5:-2])
#Python - Modify Strings
d = "Asselll"
print(d.upper())
e = "Asselll"
print(e.lower())
f = "        Hello, World! "
print(f.strip()) # returns "Hello, World!"
r = "replace"
print(r.replace("r", "u"))
t = "Hello, World!"
print(t.split(",")) # returns ['Hello', ' World!']
#Python — конкатенация строк
s="Assel "
w="is a programmer"
q=s+w
print(q)
#Python - Формат - Строки
age = 17
txt = f"My name is Assel, I am {age}"
print(txt)
#Python - Экранированные символы
txt2 = "We study  \"PP\" in the first semester."
#Python — Строковые методы
cp="hello everyone!"
print(cp.capitalize())

txt3 = "s\te\to\tp\to"
x =  txt3.expandtabs(2)
print(x)

txt4 = "nice to meet you"
y = txt4.find("meet")
print(y)