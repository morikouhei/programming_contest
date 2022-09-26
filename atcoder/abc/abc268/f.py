from functools import cmp_to_key
n = int(input())

base = 0
S = []
for i in range(n):
    s = input()
    count = 0
    x = 0
    for j in s[::-1]:
        if j == "X":
            x += 1
            base += count
        else:
            count += int(j)
    S.append([count,x])


def cmp(a,b):

    return 1 if a[0]*b[1] >= a[1]*b[0] else -1

S = sorted(S,key=cmp_to_key(cmp))

ans = base

nums = 0
for x,y in S[::-1]:
    ans += y*nums
    nums += x
print(ans)
