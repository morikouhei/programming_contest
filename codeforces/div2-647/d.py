import os,io
from sys import stdout
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline

def main():
    n,m = map(int,input().split())
    e = [[] for i in range(n)]
    for i in range(m):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        e[a].append(b)
        e[b].append(a)

    l = [[x,i] for i,x in enumerate(map(int,input().split()))]
    l.sort()
    d = [-1]*n
    ans = []
    for i in range(n):
        x,ind = l[i]
        ans.append(ind+1)
        now = 0
        s = set()
        for j in e[ind]:
            if d[j]>0:
                now = max(now,d[j])
                s.add(d[j])
        if now+1 != x or len(s) != x-1:
            print(-1)
            exit()
        d[ind] = x
        
    print(*ans)
if __name__ == "__main__":
    main()