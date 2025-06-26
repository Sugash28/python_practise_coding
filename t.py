string=input("enter your string:")
f=" "
index=0
for a in string:
    if(index%2==0):
       f=f+a
    index=index+1
print(f)
