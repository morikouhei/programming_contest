n,w = map(int,input().split())
M = 2*10**5+5
l = [0]*(M)
for i in range(n):
    s,t,p = map(int,input().split())
    l[s] += p
    l[t] -= p

for i in range(M):
    l[i] += l[i-1]
    if l[i] > w:
        print("No")
        exit()

print("Yes")
