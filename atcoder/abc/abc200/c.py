n = int(input())
A = list(map(int,input().split()))
dic = {}
ans = 0
for a in A:
    x = a%200
    ans += dic.get(x,0)
    dic[x] = dic.get(x,0)+1
print(ans)