n,q = map(int,input().split())
A = list(map(int,input().split()))
dic = {}
for i,a in enumerate(A,1):
    if a not in dic:
        dic[a] = []
    dic[a].append(i)

for i in range(q):
    x,k = map(int,input().split())

    if x not in dic:
        print(-1)
    else:
        if len(dic[x]) < k:
            print(-1)
        else:
            print(dic[x][k-1])