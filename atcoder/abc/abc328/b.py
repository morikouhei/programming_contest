n = int(input())
D = list(map(int,input().split()))
ans = 0
for i,d in enumerate(D,1):

    for j in range(1,d+1):

        s = str(i) + str(j)
        if len(set(list(s))) == 1:
            ans += 1

print(ans)