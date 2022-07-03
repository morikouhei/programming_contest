n,m = map(int,input().split())
S = list(map(int,input().split()))
X = list(map(int,input().split()))

base = [0]*n
for i in range(1,n):
    s = S[i-1]
    base[i] = s-base[i-1]

dic_0 = {}
dic_1 = {}
for i,b in enumerate(base):
    if i%2:
        dic_1[b] = dic_1.get(b,0)+1
    else:
        dic_0[b] = dic_0.get(b,0)+1


ans = 0
for i,b in enumerate(base):
    for x in X:
        dif = x-b
        count = 0
        for x in X:
            if i%2:
                count += dic_1.get(x-dif,0)
                count += dic_0.get(x+dif,0)
            else:
                count += dic_0.get(x-dif,0)
                count += dic_1.get(x+dif,0)
        ans = max(ans,count)
print(ans)