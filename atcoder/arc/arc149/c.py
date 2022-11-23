n = int(input())

if n == 3:
    ans = [[3, 9, 1], [5, 7, 8], [4, 2, 6]]
    for i in ans:
        print(*i)
    exit()

ans = [[0]*n for i in range(n)]

M = n**2+1
used = [0]*M
used[1] = used[7] = used[8] = used[14] = 1

if n%2:
    ans[n//2][n//2] = 1
    ans[n//2][n//2+1] = 8
    ans[n//2+1][n//2-1] = 7
    ans[n//2+1][n//2] = 14
else:
    ans[n//2-1][n//2-1] = 1
    ans[n//2-1][n//2] = 8
    ans[n//2][n//2-1] = 7
    ans[n//2][n//2] = 14

odd = [[] for i in range(3)]
even = [[] for i in range(3)]
for i in range(1,M):
    if used[i]:
        continue
    if i%2:
        odd[i%3].append(i)
    else:
        even[i%3].append(i)

for i in range(n-2):
    for j in range(3):
        if odd[j] and even[(3-j)%3]:
            x,y = odd[j].pop(),even[(3-j)%3].pop()
            used[x] = used[y] = 1
            if i < (n-1)//2:
                if n%2:
                    ans[i][n//2] = x
                    ans[i][n//2+1] = y
                else:
                    ans[i][n//2-1] = x
                    ans[i][n//2] = y
            else:
                ans[i+2][n//2-1] = x
                ans[i+2][n//2] = y
            break


odd = 1
even = 2
for i in range(n):
    for j in range(n):
        if ans[i][j]:
            continue
        if j < n//2:
            while used[odd]:
                odd += 2
            ans[i][j] = odd
            used[odd] = 1
        else:
            while used[even]:
                even += 2
            ans[i][j] = even
            used[even] = 1

for i in ans:
    print(*i)