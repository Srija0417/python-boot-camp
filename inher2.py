class Kiran:
    def kirans():
        return "im the father"
class Karina:
    def karinas():
        return "im the mother"
class Katt(Kiran,Karina):
    def katty():
        return("im the child")    
obj1=Kiran        
obj2=Karina
obj3=Katt
print(obj3.karinas())  # kid obj tho any feature osthadi but parent obj tho only parent feature eh osthasdi
print(obj3.kirans())
print(obj3.katty())
print(obj2.karinas())
print(obj1.kirans())


