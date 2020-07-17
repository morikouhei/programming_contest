n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
d = {}
for i in range(n):
    d[a[i]] = i
ans = [0]*n
for i in range(n):
    j = d[b[i]]
    ans[(j-i)%n] += 1
print(max(ans))