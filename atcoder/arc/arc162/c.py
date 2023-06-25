def solve():
    n,k = map(int,input().split())

    e = [[] for i in range(n)]

    P = list(map(int,input().split()))
    for i,p in enumerate(P,1):
        p -= 1
        e[p].append(i)
        e[i].append(p)

    P = [-1] + P

    A = list(map(int,input().split()))
    for i in range(n):

        num = 0
        s = set()
        q = [i]
        while q:
            now = q.pop()
            if A[now] == -1:
                num += 1
            else:
                s.add(A[now])

            for nex in e[now]:
                if nex == P[now]-1:
                    continue
                q.append(nex)
        
        mex = -1
        need = [0]*(k+1)
        for j in range(k+1):
            if j in s:
                need[j] = 1
        
        if need[k] or num > 1:
            continue

        count = 0
        for j in range(k):
            if need[j] == 0:
                count += 1
        
        
        if count == 0:
            return "Alice"
        
        if count == 1 and num == 1:
            return "Alice"
    
    return "Bob"

t = int(input())
for _ in range(t):
    print(solve())
        
