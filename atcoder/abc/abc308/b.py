n,m = map(int,input().split())
C = input().split()
D = input().split()
P = list(map(int,input().split()))
dish = {d:p for d,p in zip(D,P[1:])}

ans = 0
for c in C:
    ans += dish.get(c,P[0])
print(ans)