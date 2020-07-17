t = int(input())
for _ in range(t):
    a,b,n,m = map(int,input().split())
    if a+b >= n+m and m <= min(a,b):
        print("Yes")
    else:
        print("No")