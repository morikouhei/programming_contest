import sys, os, io
input = lambda: sys.stdin.readline().rstrip('\r\n')

def solve():
    M = 10**7
    count = [1]*(M+1)
    ans = [-1]*(M+1)
    ans[1] = 1
    for i in range(2,M+1):
        now = i
        while now <= M:
            count[now] += i
            now += i
        num = count[i]
        if num > M or ans[num] > 0:
            continue
        ans[num] = i
    return ans

ans = solve()


t = int(input())
X = [int(input()) for i in range(t)]
res = [ans[x] for x in X]
for i in res:
    print(i)