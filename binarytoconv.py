def sort(a):
    length=len(a)
    for i in range(length):
        for j in range(length):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
                
    print(a)
    btd(a)
def btd(a):
    f=0
    b=0
    for i in range(len(a)-1):
        b+=a[(len(a)-1)-i]*(2**f)
        f=f+1
    print(b)
n=int(input())
a=[]
while n>0:
    c=int(n%2)
    
    a.append(c)
    n=int(n/2)
a.reverse()
sort(a)