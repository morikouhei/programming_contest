t = int(input())
for _ in range(t):
    n,m,k = map(int,input().split())
    cost = n-1+(m-1)*n
    cost2 = m-1+(n-1)*m
    if cost == k or cost2 == k:
        print("Yes")
    else:
        print("No")