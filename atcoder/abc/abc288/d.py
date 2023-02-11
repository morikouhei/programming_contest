n,k = map(int,input().split())
A = list(map(int,input().split()))
dif = [0]
for a,na in zip(A,A[1:]):
    dif.append(na-a)
print(dif)
q = int(input())
LR = [list(map(int,input().split())) for i in range(q)]
# for l,r in LR:
#     l -= 1
#     print("Yes" if dif[l] == dif[r] else "No")