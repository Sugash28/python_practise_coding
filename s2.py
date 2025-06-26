a=[2,4,6,5,-1,-1,-2,3]
cur=a[0]
maxa=a[0]
for num in a[1:]:
    cur=max(num,maxa+num)
    maxa=max(cur,maxa)
print(maxa) 

def sort(b):
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i]>b[j]:
                b[i],b[j]=b[j],b[i]
    return b 


def largesubarray(b):
    n=int(input())
   # lena=len(b)+1
    f=sort(b)
    c=f[0:n]
    print(c)





b=list(map(int,input().split()))
largesubarray(b)


    