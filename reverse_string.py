x=-123
string_num=str(abs(x))
string_num=string_num[::-1]
if x<0:
    string_num='-' + string_num
    print(int(string_num))
else:
    print(int(string_num))
