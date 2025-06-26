def pat():
    n=5
    for i in range(1,n+1):
        print('* '*i)
    
def py():
    n=5
    for i in range(1,n+1):
        print(' '*(n-i)+'* '*i)
def inpy():
    n=5
    for i in range(n-1,0,-1):
        print(' '*(n-i)+'* '*i)

pat()  
py()
inpy()