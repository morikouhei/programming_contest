n = int(input())
count = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,input().split())
    count[a] += 1
    count[b] += 1
if max(count) == n-1:
    print("Yes")
else:
    print("No")