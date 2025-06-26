from abc import abstractmethod,ABC

class a(ABC):
    @abstractmethod
    def h(self):
        print("hi")
class b(a):
    def h(self):
        super().h()
        print("hello")
        
c=b()
c.h()