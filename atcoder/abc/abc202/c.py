n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))

cand = [0]*(n+5)
for c in C:
    cand[B[c-1]] += 1

ans = 0
for a in A:
    ans += cand[a]
print(ans)