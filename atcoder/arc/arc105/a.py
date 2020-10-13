l = list(map(int,input().split()))

l.sort()
if l[-1]*2 == sum(l):
    print("Yes")
    exit()
if l[-1]+l[0] == l[1]+l[2]:
    print("Yes")
    exit()
print("No")