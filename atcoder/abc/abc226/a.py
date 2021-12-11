x = input()
num = 0
flag = 0
for i in x:
    if i == ".":
        flag = 1
        continue
    if flag:
        if int(i) < 5:
            print(num)
        else:
            print(num+1)
        exit()
    
    else:
        num *= 10
        num += int(i)
