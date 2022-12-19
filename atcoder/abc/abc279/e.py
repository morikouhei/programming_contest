n,m = map(int,input().split())
A = list(map(int,input().split()))

B = [i+1 for i in range(n)]
front = [1]
pos = 1
for a in A:
    if pos == a:
        pos += 1
    elif pos == a+1:
        pos -= 1
    front.append(pos)

ans = [0]*m
ans[-1] = front[-2]
for i in range(m-1)[::-1]:
    a = A[i+1]
    B[a-1],B[a] = B[a],B[a-1]
    
    pos = front[i]
    ans[i] = B[pos-1]
for i in ans:
    print(i)