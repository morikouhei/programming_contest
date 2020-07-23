t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    ans = n
    now = 0
    count = 0
    li = 0
    for i in l[::-1]:
        if i >= now:
            now = i
            count += 1
        else:
            li = count
            break
    if count == n:
        print(0)
        continue
    for i in range(li,n):
        if now >= l[-i-1]:
            now = l[-i-1]
            
            count += 1
        else:
            break
    print(n-count)

            
