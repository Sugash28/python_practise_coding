a =[4,3,2,1,4]

left=0
right=len(a)-1
max_area=0

while left<right:
    width=right-left
    ht=min(a[left],a[right])
    area=width*ht
    max_area=max(max_area,area)
    if a[left]<a[right]:
        left+=1
    else:
        right-=1
        
print( max_area)
        

    