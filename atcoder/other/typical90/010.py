n = int(input())
cum1 = [0]
cum2 = [0]
for i in range(n):
    c,p = map(int,input().split())
    if c == 1:
        cum1.append(cum1[-1]+p)
        cum2.append(cum2[-1])
    else:
        cum1.append(cum1[-1])
        cum2.append(cum2[-1]+p)

q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(cum1[r]-cum1[l-1],cum2[r]-cum2[l-1])
