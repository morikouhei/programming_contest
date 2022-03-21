n = int(input())
T = input()
dx = [1,0,-1,0]
dy = [0,-1,0,1]
now = 0
x = 0
y = 0
for s in T:
    if s == "S":
        x += dx[now]
        y += dy[now]
    else:
        now = (now+1)%4
print(x,y)