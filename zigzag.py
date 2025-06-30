def zigzag(s, num):
    si=[]
    start=0
    end=num
    dummy=num
    while num+1>0:
        si.append(s[start:end])
        num=num-1
        start=end+(dummy-2)
        end=start+dummy
        if end >len(s):
            end=len(s)
        #print(start,end)
    si=[item for item in si if item.strip()]
    lenght=len(si)
    finall=[]
    y=0
    for i in range(lenght-1):
        dum=lenght
        x=0
        while dum>0:
            if x < len(si) and i < len(si[x]):
                finall.append(si[x][i])
                x+=1
                dum=dum-1
                #print(i,x)    
            else:
                break
    g=[]
    constant=dummy
    dumm=dummy
    while dumm>0 and constant<len(s):
        finall.insert(constant+2,s[constant])
        constant+=dummy+1
        dumm-=1
        print(constant)
    print(g)
        
    return finall


s="PAYPALISHIRING"
NUM=3
print(zigzag(s,NUM))
