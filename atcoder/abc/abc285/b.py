n = int(input())
S = input()
for i in range(1,n):
    ans = 0
    for j in range(n):
        if i+j >= n:
            break
        if S[j] == S[j+i]:
            break
        ans = j+1
    print(ans)