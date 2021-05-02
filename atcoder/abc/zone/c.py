n = int(input())
L = [list(map(int,input().split())) for i in range(n)]


def check(x):
    s = set()
    for l in L:
        c = 0
        for i in range(5):
            if l[i] >= x:
                c |= 1<<i
        s.add(c)

    s = list(s)+[0]*2
    le = len(s)

    for i in range(le):
        for j in range(i):
            for k in range(j):
                if s[i]|s[j]|s[k] == 31:
                    return True

    return False

l = 0
r = 10**9+5

while r > l + 1:
    m = (r+l)//2
    if check(m):
        l = m
    else:
        r = m
print(l)

