s="abcda"
def isplaindrome(s):
            if s==s[::-1] and len(s)>1:
                return True
            else:
                return False
a=[]
maxx=0 
strinf=""
if len(s)<3 and s[len(s)-1]!=s[len(s)-2]:
    print(s[0])
elif len(s)<2:
    print(s)
else:
    for i in range(len(s)):
        for j in range(len(s)-1,-1,-1):
            if s[i]==s[j]:  
                 if len(s)<3 and s[i]!=s[j]:
                    print(s[i])
                 elif isplaindrome(s[i:j+1]):
                    a.append(s[i:j+1])
                 
for i in range(len(a)):
    if len(a[i])>maxx:
        maxx=len(a[i])
        strinf=a[i]
    
print(maxx)
print(a)
print(strinf)
    

