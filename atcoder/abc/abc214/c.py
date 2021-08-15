n = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

ans = T[:]
time = 10**20
for i in range(2*n):
    time = min(time,T[i%n])
    ans[i%n] = min(ans[i%n],time)
    time += S[i%n]
for i in ans:
    print(i)