n = int(input())
A = list(map(int,input().split()))

num = 0
l = []
for a in A:
    if l:
        if l[-1][0] == a:
            l[-1][1] += 1
            num += 1

        else:
            l.append([a,1])
            num += 1

        if l[-1][0] == l[-1][1]:
            num -= l[-1][1]
            l.pop()
    else:
        l.append([a,1])
        num += 1
    print(num)
