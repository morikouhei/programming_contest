import collections
n = int(input())
A = list(map(int,input().split()))

C = collections.Counter(A)


def calc(x):

    left = 0
    
    l = []
    for key,value in C.items():
        if key <= x:
            l.append(key)
            left += value-1
        else:
            left += value
    l.sort()
    # print(l,left,x)
    last = 0
    for i in l:
        # print(i,last,left)
        if i == last+1:
            last = i
            continue
        dif = i-last-1
        # print(dif)
        if dif <= left//2:
            left -= dif*2
            last = i
        else:
            return False
    # print("here")
    if last < x:
        dif = x-last
        if dif*2 <= left:
            return True
        else:
            return False
    else:
        return True

l = 0
r = n+2

while r > l + 1:
    m = (r+l)//2
    if calc(m):
        l = m
    else:
        r = m
print(l)