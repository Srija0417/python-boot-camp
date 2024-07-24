class Animal:
    def animal():
        return"parent"
class Dog(Animal):
    def animal():
        return "kid"
class Puppy(Dog):
    def animal():
        return "grandkid"    
obj=Animal
obj1=Dog
obj2=Puppy               #obj de output osthadi 
print(obj2.animal())   
print(obj.animal())
print(obj1.animal())
