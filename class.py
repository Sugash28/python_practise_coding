class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def print(self):
         print(f"{self.name}")
class b(a):
    def __init__(self,name,age):
        super().__init__(name,age)
    def print(self):
        super().print()
       # return f"{self.name}:{self.age}"
    
ans=b("arr",23)
ans.print()


        
        