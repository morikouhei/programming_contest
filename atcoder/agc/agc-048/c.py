from collections import defaultdict
n,l = map(int,input().split())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = 0
dic = {}
dic[1] = -1
for i in range(n):
    if a[i] <= b[i]:
        dic[a[i]-i] = i
        continue
    if b[i]-i not in dic:
        print(-1)
        exit()
    ans += i-dic[b[i]-i]
    dic[b[i]-i] = i
    dic[a[i]-i] = i
dic = {}
dic[l-n+1] = n
for i in range(n-1,-1,-1):
    if a[i] >= b[i]:
        dic[a[i]-i] = i
        continue
    if b[i]-i not in dic:
        print(-1)
        exit()
    ans += dic[b[i]-i]-i
    dic[b[i]-i] = i
    dic[a[i]-i] = i
print(ans)
