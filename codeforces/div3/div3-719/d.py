from collections import defaultdict
t = int(input())
for _ in range(t):
    n = int(input())
    A = list(map(int,input().split()))
    dic = defaultdict(int)
    ans = 0
    for i,a in enumerate(A):
        ans += dic[a-i]
        dic[a-i] += 1
    print(ans)