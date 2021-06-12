def solve():
    n = int(input())
    T = list(map(int,input().split()))

    if len(set(T)) == 1:
        col = 1
        ans = [1]*n
    elif n%2 == 0:
        col = 2
        ans = [1,2]*(n//2)
    else:
        ind = -1
        for i in range(n):
            if T[i] == T[(i+1)%n]:
                ind = i
                break
        if ind == -1:
           col = 3
           ans = [1,2]*(n//2)
           ans.append(3)
        else:
            col = 2
            ans = [1]*n
            for i in range(2,n,2):
                ans[(ind+i)%n] = 2
    print(col)
    print(*ans)



t = int(input())
for _ in range(t):
    solve()