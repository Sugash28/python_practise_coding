#encapsulation
class a:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def setname(self,name):
        self.__name=name
    def getname(self):
        return self.__name
    
class b(a):
    def __init__(self,name,age):
        super().__init__(name,age)
        
b=a("aa",33)
b.setname("avv")
print(b.getname())