#A recipe you are reading states how many grams you need for the ingredient. Unfortunately, your store only sells items in ounces. 
#1. Create a function to convert grams to ounces. ounces = 28.3495231 * grams
def gramms(gr):
    ounces= gr*28.3495231
    return ounces
print(gramms(100))
#2. Read in a Fahrenheit temperature. 
def faren(fr):
    c=(5/9)*(fr-32)
    return c
print(faren(int(input())))
#3. 
def count(heads,legs):
    rab=(legs-2*heads)//2
    chickens=heads-rab
    return rab,chickens
rab,chickens=count(35,94)
print(rab,chickens, sep=" , ")
#4.
def prime(n):
    if n < 2:  
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primerange(start, end):
    primes = []  
    for num in range(start, end + 1):
        if prime(num): 
            primes.append(num)
    return primes
def filter_prime(numbers):
    primes = []  
    for num in numbers:  
        if prime(num):  
            primes.append(num)  
    return primes 
numbers = list(map(int, input().split()))
primes = filter_prime(numbers)
print( *primes) 
#5. 
def st(s):
    if len(s)==1:
        return s
    new=[]
    for i in range(len(s)):
        for j in st(s[:i]+s[i+1:]):
            new.append(s[i]+j)
    return new
print(*st(input()), sep=" , ")
#6. 
def sy():
    sentence=input()
    word = sentence.split()
    return word[::-1]
print(*sy()) 
#7 
def rt(lew = []):
    for i in range(0,len(lew)):
        if ((lew[i]==3) and lew[i+1]==3):
            return True
    return False
#8 
def gh(large=[]):
    cout=0
    for i in range(0,len(large)):
        if((large[i]==0)):
            cout+=1
        elif ((large[i]==7)and cout==2):
            return True 
    return False
#9 
def volume(r):
    pi=3.14
    return (4/3)*(pi)*(r**3)
#10 
def uset(lst):
    lst.sort
    ulst = []
    for i in lst:
        if i not in ulst:
            ulst.append(i)
    return ulst
#11 palindrome
def pl(str):
    rev=str[::-1]
    if rev==str:
        return True
    return False
#12 histogram
def his(lis):
    for i in lis:
        print(i*'*')
#13 guess the number
import random 
def game():
    guessnum=random.randint(1,25)
    print("Hello! What is your name?")
    name=input()
    print("Well, " ,name ,", I am thinking of a number between 1 and 20.")
    print("Take a guess")
    coun=0
    while True:
        num=int(input())
        if num<guessnum:
            print("Your guess is too low.")
            coun+=1
        elif num>guessnum:
            print("Your guess is too high.")
            coun+=1
        elif num==guessnum:
            print("Good job, KBTU! You guessed my number in", coun ," guesses!")
