import itertools
import bisect
n,x = map(int,input().split())


cand = [[] for i in range(10)]
cand2 = [[] for i in range(10)]
for l in itertools.permutations(range(n),n):

    A = []
    lis = []
    for x,nx in zip(l,l[1:]):
        A.append(abs(x-nx))
        if lis and bisect.bisect_left(lis,A[-1]) < len(lis):
            lis[bisect.bisect_left(lis,A[-1])] = A[-1]
        else:
            lis.append(A[-1])
    # print(A,lis,l)
    t = l[0]
    if cand[t] == []:
        cand[t] = [lis]
        cand2[t] = [l]
    elif cand[t] and len(cand[t][0]) < len(lis):
        cand[t] = [lis]
        cand2[t] = [l]
    elif cand[t] and len(cand[t][0]) == len(lis):
        cand[t].append(lis)
        cand2[t].append(l)


for i in range(n):
    print(i)
    for x,y in zip(cand[i],cand2[i]):
        print(*x)
        print(*y)