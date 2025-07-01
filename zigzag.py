def zigzag(s, num):
   if num == 1 or num >= len(s):
       return s
   rows=['']*num
   index=0
   step=1
   
   for char in s:
       rows[index]+=char
       if index==0:
           step=1
       elif index==num-1:
            step=-1
       index+=step
   return ''.join(rows)
   


s="PAYPALISHIRING"
NUM=4
print(zigzag(s,NUM))
