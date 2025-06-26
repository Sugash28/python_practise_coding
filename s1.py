class Dog:
    a="mammal"
    def __init__(self,name):
        self.name=name
    def speak(self):
        print("my name",self.name)
        
r=Dog("rrr")
r.speak()

