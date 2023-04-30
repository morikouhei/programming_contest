n = int(input())
A = list(map(int,input().split()))

ans = 0

ten = 1
for i in range(16):
    ten *= 10

    sA = sorted([a%ten for a in A])

    dx = ten//10

    pos = [n-1]*21
    targets = [dx*i for i in range(21)]
    for i,a in enumerate(sA):
        for j in range(21)[::-1]:
            target = targets[j]
            while pos[j] >= 0 and sA[pos[j]] >= target-a:
                pos[j] -= 1
        for j in range(20):
            ans += (pos[j+1]-pos[j])*(j%10)

print(ans)
