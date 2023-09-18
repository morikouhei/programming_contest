n = int(input())
A = list(map(int,input().split()))

e = [[] for i in range(n)]
for i,a in enumerate(A):
    e[a-1].append(i)


ans = 0

for x in e:
    if x == []:
        continue
    s = len(x)

    num = 0
    ind = 0
    for i,a in enumerate(x):

        ans -= i * (s-i-1)

        ans += num * a - ind

        num += 1
        ind += a+1
print(ans)