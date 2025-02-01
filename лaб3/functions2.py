# Dictionary of movies

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]
#1 
def reit(movies):
    if movies["imdb"]>5.5:
        return True
    return False
print(reit(movies[4]))
#2 
def pup(movies):
    for i in movies:
        high=[]
        if i["imdb"]>5.5:
         high.append(i)
         return high
print(pup(movies),'\n' )
#3
def categorys(category):
   inf=[]
   for i in movies:
      if i["category"]== category:
        inf.append(i["name"])
        return inf
print(categorys("Adventure"))
#4 
def avr():
   lirt=[]
   avg=0
   coun=0
   for i in movies:
      avg+=i["imdb"]
      coun+=1
      result=avg/coun
      return result
print(avr())
#5
def catavr(category):
   avg=0
   coun=0
   for i in movies:
      if i["category"]==category:
         avg+=i["imdb"]
         coun+=1
         res=avg/coun
         return res
print(catavr("Romance"))