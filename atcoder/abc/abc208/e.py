n,k = map(int,input().split())
l = len(str(n))
dic1 = {}
dic2 = {}
x = int(str(n)[0])
for i in range(1,x+1):
    if i != x:
        dic2[i] = 1
    else:
        dic1[i] = 1
for i in str(n)[1:]:
    x = int(i)
    ndic1 = {}
    ndic2 = {}
    for num,c in dic1.items():
        for j in range(x+1):
            if j < x:
                ndic2[num*j] = ndic2.get(num*j,0)+c
            else:
                ndic1[num*j] = ndic1.get(num*j,0)+c
    for num,c in dic2.items():
        for j in range(10):
            if j < x:
                ndic2[num*j] = ndic2.get(num*j,0)+c
            else:
                ndic2[num*j] = ndic2.get(num*j,0)+c
    for j in range(1,10):
        ndic2[j] = ndic2.get(j,0)+1

    dic1 = ndic1
    dic2 = ndic2
ans = 0
for num,c in dic1.items():
    if num <= k:
        ans += c

for num,c in dic2.items():
    if num <= k:
        ans += c
print(ans)