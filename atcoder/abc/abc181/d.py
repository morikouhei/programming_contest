import copy
s = list(input())
l = [int(i) for i in s]
if len(l) == 1:
    if l[0] == 8:
        print("Yes")
    else:
        print("No")
    exit()
if len(l) == 2:
    if (l[0]*10+l[1])%8 == 0 or (l[1]*10+l[0])%8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

count = [0]*10
for i in l:
    count[i] += 1

for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            d = copy.deepcopy(count)
            d[i] -= 1
            d[j] -= 1
            d[k] -= 1
            if d[i] >= 0 and d[j] >= 0 and d[k] >= 0:
                cal = 100*i+10*j+k
            
                if cal%8 == 0:
                    print("Yes")
                    exit()
print("No")