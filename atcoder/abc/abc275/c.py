S = [input() for i in range(9)]
ans = 0
n = 9
lis = []
for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            lis.append([i,j])

def check(i,j,k):
    x1,y1 = lis[i]
    x2,y2 = lis[j]
    x3,y3 = lis[k]
    x4,y4 = x1+x2-x3,y1+y2-y3
    if 0 <= x4 < n and 0 <= y4 < n and S[x4][y4] == "#":
        if (x1-x2)**2 + (y1-y2)**2 == (x4-x3)**2 + (y4-y3)**2:
            if (x1-x3)**2 + (y1-y3)**2 == (x1-x4)**2 + (y1-y4)**2:
                return (x4,y4)

    return (-1,-1)

def is_square(i,j,k):
    l = set()

    a = check(i,j,k)
    if a != (-1,-1):
        l.add(a)
    a = check(i,k,j)
    if a != (-1,-1):
        l.add(a)
    a = check(j,k,i)
    if a != (-1,-1):
        l.add(a)
    return len(l)
    

    

for i in range(len(lis)):
    for j in range(i):
        for k in range(j):
            ans += is_square(i,j,k)
print(ans//4)                
