class Person():
    def __init__ (self,name,age):
        self.name=name
        self.age=age
class student(Person):
    def __init__ (self,id,name,age):
        super.__init__(name,age)
        self.id=id
    
    