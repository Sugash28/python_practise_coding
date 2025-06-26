s=set({1,2,3,4,5,64,2,3,1,2,3,4})
u={6,7,8,9,10}
print(s|u)
print(s&u)
print(s-u)
print(s^u)
set1={1,23,4,4,5,34}
set2={1,234,44,3,4,2}
set3={1,22,22,2,34,4}
set4=set1&set2&set3
print(set4)
for key,val in enumerate(set1):
    print(key, val)
set5={5}
set5.discard(5)
print(set5)
#set5.remove(5)
#print(set5)
set6={2,4,5,7,8}
set6.pop()
set6.pop()
print(set6)

