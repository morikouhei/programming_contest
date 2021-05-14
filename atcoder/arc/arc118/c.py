n = int(input())
s = set()
for i in range(2,n):
    s.add(6*i)
    s.add(10*i)
    s.add(15*i)

ans = [6,10,15]
l = sorted(set(s))
for i in range(n-3):   
    ans.append(l[i])
print(*ans)