t = int(input())
for _ in range(t):
    n,c = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))+[0]
    ans = 10**20
    have = 0
    day = 0
    for i in range(n):
        ans = min(ans,day+(c-have+A[i]-1)//A[i])
        need = (B[i]-have+A[i]-1)//A[i]
        have += need*A[i]
        day += need+1
        have -= B[i]

    print(ans)
        