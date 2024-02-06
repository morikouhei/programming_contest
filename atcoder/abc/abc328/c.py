n,q = map(int,input().split())
S = input()

cums = [0,0]

count = 0
for s,ns in zip(S,S[1:]):
    if s == ns:
        count += 1
    cums.append(count)
for _ in range(q):
    l,r = map(int,input().split())
    print(cums[r]-cums[l])