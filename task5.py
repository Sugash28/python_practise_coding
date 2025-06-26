def count(n,k):
    for i,y in enumerate(n):
            if k==i:
                return y
            else:
                return count(n,k)
            
n=input("enter the number:")
k=int(input("enter the number:"))
a=count(n,k)
 
if count != None:
    print(a)
else:
    print("out of range")
   
        