def normalmethod(string):
    f=" "
    index=0
    for a in string:
        if(index%2==0):
            f=f+a
        index=index+1
    print(f)
def usingenumeratefunction(string):
    f=" "
    for i,a in enumerate(string):
        if(i%2==0):
            f=f+a
    print(f)
string=input("enter the college name:")
while True:
    print("1.method1")
    print("2.Method2")
    ch=int(input("ENTER THE OPTION:"))
    if ch==1:
        normalmethod(string)
    elif ch==2:
        usingenumeratefunction(string)
    