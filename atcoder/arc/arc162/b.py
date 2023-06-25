n = int(input())
P = list(map(int,input().split()))

invs = 0
for i in range(n):
    for j in range(i):
        if P[i] < P[j]:
            invs += 1

if invs%2:
    print("No")
    exit()

print("Yes")
ans = []
while True:

    end = 1
    for i in range(n):
        if P[i] != i+1:
            end = 0
            x = i
            break

    if end:
        break

    for i in range(n):
        if P[i] == x+1:
            y = i
            break
    
    if y == n-1:
        y -= 1

    ans.append([y+1,x])

    a = P[y:y+2]
    lP = P[:y] + P[y+2:]
    P = lP[:x] + a + lP[x:]
        
print(len(ans))
for a,b in ans:
    print(a,b)