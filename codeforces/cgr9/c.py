t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    dif = 0
    for i in range(1,n):
        dif += l[i]-l[i-1]
    if dif > 0:
        print("YES")
    else:
        print("NO")