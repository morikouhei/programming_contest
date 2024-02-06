import itertools
h,w = map(int,input().split())

ans = 10**10



def calc(l):

    num = 0

    for i in range(len(l)):
        for j in range(i):
            if l[i] < l[j]:
                num += 1
    return num

A = [list(map(int,input().split())) for i in range(h)]
B = [list(map(int,input().split())) for i in range(h)]


for H in itertools.permutations(range(h),h):

    for W in itertools.permutations(range(w),w):

        ok = 1

        for i in range(h):
            for j in range(w):
                if B[i][j] == A[H[i]][W[j]]:
                    continue
                ok = 0
        
        if ok == 0:
            continue

        num = calc(list(H))+calc(list(W))

        ans = min(ans,num)

if ans == 10**10:
    ans = -1

print(ans)