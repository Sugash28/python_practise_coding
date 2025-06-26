class python:
   def _init_(self,real = 0,imag = 0):
       print("mycomplexnumber constructor executing...")
       self.real_part = real
       self.imag_part = imag
   def displaycomplex(self):
        print("{0} + {1}j".format(self.real_part,self.imag_part))
        cmp = mycomplexnumber(40,50)
        cmp.displaycomplex()
