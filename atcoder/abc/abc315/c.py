n = int(input())
FS = [list(map(int,input().split())) for i in range(n)]

F = [[] for i in range(n)]
for f,s in FS:
    F[f-1].append(s)


ans = 0
mas = []
for f in F:
    if f == []:
        continue

    f.sort()
    mas.append(f[-1])

    if len(f) >= 2:
        ans = max(ans,f[-1]+f[-2]//2)

mas.sort()

if len(mas) >= 2:
    ans = max(ans,mas[-1]+mas[-2])
print(ans)