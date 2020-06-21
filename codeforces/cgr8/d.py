n = int(input())
l = list(map(int,input().split()))
count = [0]*21
for i in l:
    for j in range(21):
        if i >> j & 1:
            count[j] += 1
ans = 0
for i in range(n):
    c = 0
    for j in range(21):
        if count[j] > 0:
            count[j] -= 1
            c += 2**j
    ans += c**2
print(ans)