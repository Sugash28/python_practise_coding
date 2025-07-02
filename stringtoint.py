x="-42"
y=""


for i in x:
    if i.isdigit() :
        y+=i
    elif i == '-' and y == "":
        y = '-' + y
    else:
        break
print(int(y)) 