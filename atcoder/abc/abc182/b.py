n = int(input())
a = list(map(int,input().split()))

ans = 0
ma = 0
for i in range(2,max(a)+1):
    s = sum(j%i == 0 for j in a)
    if ma < s:
        ans = i
        ma = s
print(ans)
