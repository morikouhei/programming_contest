import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
import numpy as np

def main():
    n = int(input())
    l = [list(map(int,input().split())) for i in range(n)]
    dic = {}
    q = int(input())
    Q = []
    lm = 0
    for i in range(q):
        a,b = map(int,input().split())
        lm = max(b,lm)
        Q.append((a,b))
    d = np.zeros(lm+1,dtype=np.int64)
    if l[0][1] <= lm:
        d[l[0][1]] = l[0][0]
    dic[1] = d
    
    def dfs(x):
        if x in dic:
            return dic[x]
        
        v,w = l[x-1]
        li = dfs(x//2)
        d = np.zeros(lm+1,dtype=np.int64)
        d[w:] = np.maximum(li[w:],li[:-w]+v,out=li[w:])
        dic[x] = d
        return d

    for a,b in Q:
        s = dfs(a)
        print(np.max(s[:b+1]))
if __name__ == "__main__":
    main()