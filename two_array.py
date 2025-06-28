a=[]
b=[1,2,3,4,5,6]

for num in b:
    a.append(num)
a=sorted(a)

if len(a)<3:
    lenght=len(a)
    #print(lenght)
    if lenght %2==0:
        medians =a[int(lenght-1)]+a[int(lenght-2)]
        print(medians/2)
else:
    
    lenght=len(a)/2
if len(a) %2==0:
    median =a[int(lenght-1)]+a[int(lenght)]
    print("printed",median/2)
else:
    if len(a)<2:
        print("No median")
        median =a[int(lenght-1)]
        print(median)
    else:
        
        median =a[int(lenght)]
        print(median)

    
