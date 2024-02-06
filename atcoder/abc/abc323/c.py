n,m = map(int,input().split())
A = list(map(int,input().split()))
S = [input() for i in range(n)]

ma = 0
for i,s in enumerate(S,1):
    score = i
    for j in range(m):
        if s[j] == "o":
            score += A[j]
    ma = max(ma,score)


for i,s in enumerate(S,1):
    score = i
    left = []
    for j in range(m):
        if s[j] == "o":
            score += A[j]
        else:
            left.append(A[j])

    if score == ma:
        print(0)
        continue
    left.sort(reverse=True)
    for j,a in enumerate(left,1):
        score += a
        if score > ma:
            print(j)
            break