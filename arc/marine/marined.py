n = int(input())
a = [int(input()) for i in range(n)]
a.sort()

p = [0]*n
m = [0]*n

for i in range(n-1):
    if i%2:
        m[i] += 1
        p[i+1] += 1
    else:
        p[i] += 1
        m[i+1] += 1
p.sort(reverse=True)
m.sort(reverse=True)
ans = 0
print(p,m)
for i in range(n):
    if m[i] <= 0:
        break
    ans -= m[i]*a[i]
for i in range(n):
    if p[i] <= 0:
        break
    ans += p[i]*a[-1-i]
ans2 = 0
for i in range(n):
    if p[i] <= 0:
        break
    ans2 -= p[i]*a[i]
for i in range(n):
    if m[i] <= 0:
        break
    ans2 += m[i]*a[-1-i]
print(ans,ans2)
print(max(ans,ans2))
