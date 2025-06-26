import math
def fact(k):
    if k==1:
        return k
    else:
        return(k*fact(k-1))
def sum(k):
    m=0
    while k>0:
        m=m+(fact(k)/k)
        k=k-1
        return int(sum)
    
def  mat(g):
    for num in g:
      f=math.factorial(num)/num
    return f
        
k=int(input("Enter the numbers:"))
b=sum(k)
print(b)
f=input("enter the list of numbers:")
g=list(map(int,f.split()))
c=mat(g)
print(c)
