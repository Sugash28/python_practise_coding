def addtwonumbers(l1,l2):
    o1=""
    o2=""
    final=[]
    for i in l1:
        o1=str(i)+o1
    for j in l2:
        o2=str(j)+o2
    sum1=int(o1)+int(o2)
    for k in str(sum1):
        final.append(int(k))
    return final
    
    




l1=[2,4,3]
l2=[5,6,4]
output=addtwonumbers(l1,l2)
print(output)