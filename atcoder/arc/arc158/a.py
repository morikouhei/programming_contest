def solve():
    X = sorted(list(map(int,input().split())))

    dx = [X[1]-X[0],X[2]-X[1]]
    if dx[0]%2 or dx[1]%2:
        return -1

    ans = min(dx)//2

    left = sum(dx)-min(dx)*2

    if left%6:
        return -1
    
    ans += left//3

    return ans

t = int(input())
for _ in range(t):
    print(solve())