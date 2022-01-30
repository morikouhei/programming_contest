n,m = map(int,input().split())
S = list(input().split())
T = list(input().split())
T = set(T)
for s in S:
    if s in T:
        print("Yes")
    else:
        print("No")