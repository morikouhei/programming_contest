S = input()
dic = {}
b = 0
c = 0
for s in S:
    if s in dic:
        print("No")
        exit()
    if "A" <= s <= "Z":
        b = 1
    else:
        c = 1
    dic[s] = 1
if b and c:
    print("Yes")
else:
    print("No")