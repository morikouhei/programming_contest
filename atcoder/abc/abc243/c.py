
n = int(input())
XY = [list(map(int,input().split())) for i in range(n)]
S = input()

dic = {}
for s,(x,y) in zip(S,XY):
    if y not in dic:
        dic[y] = [10**10,-10**10]
    if s == "R":
        dic[y][0] = min(dic[y][0],x)
    else:
        dic[y][1] = max(dic[y][1],x)

for v in dic.values():
    if v[0] < v[1]:
        print("Yes")
        exit()
print("No")