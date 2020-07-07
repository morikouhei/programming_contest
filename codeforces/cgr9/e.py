n = int(input())
l = list(map(int,input().split()))
l2 = sorted(l)

ans = []
for i in range(n-1,0,-1):
    if l[i] == l2[i]:
        continue
    for j in range(i):
        if l[j] == l2[i]:
            l[j],l[i] = l[i],l[j]
            ans.append([j+1,i+1])
            break
    
print(len(ans))
for i in ans:
    print(*i)