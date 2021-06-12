def solve():
    n,m = map(int,input().split())
    dic = {}
    s = set()
    for i in range(m):
        x,y = map(int,input().split())
        dic[y] = dic.get(y,0) | 1<<(x-1)
        s.add(y)
    dic[2*10**9] = 3
    s.add(2*10**9)
    last = 0
    col = 0
    for x in sorted(list(s)):
        mask = dic[x]
        if mask != 3 and last:
            ncol = (x+mask)%2
            if col == ncol:
                print("NO")
                return
            else:
                last = 0
        elif mask == 3 and last:
            print("NO")
            return
        elif mask != 3:
            col = (x+mask)%2
            last = 1
    print("YES")
    return


t = int(input())
for _ in range(t):
    x = input()
    solve()