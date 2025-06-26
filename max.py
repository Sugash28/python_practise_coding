a=[1,6,3]
l=len(a)
k=7
large=0

for i in range(k):
    sum=0
    for j in range(l): 
        
        sum+=a[j]^i 
#        print(sum)
        
    if sum>large:
        large=sum
print(large)
            

        