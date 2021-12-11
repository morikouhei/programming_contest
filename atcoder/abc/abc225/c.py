n,m = map(int,input().split())
B = [list(map(int,input().split())) for i in range(n)]
s = B[0][0]-1
x,y = divmod(s,7)
print(x,y)
if 7-y < m:
    print("No")
    exit()
num = s
for i in range(n):
    now = num
    for j in range(m):
        if B[i][j] != num+1:
            print("No")
            exit()
        num += 1
    num = now+7
print("Yes")