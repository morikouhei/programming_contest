t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    l = [0]*3
    for a in A:
        l[a%3] += 1
    ans = 0
    while min(l) != n//3:
        for i in range(3):
            if l[i] > n//3:
                l[i] -= 1
                l[(i+1)%3] += 1
                ans += 1
    print(ans)