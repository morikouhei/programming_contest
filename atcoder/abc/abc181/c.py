n = int(input())
xy = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for k in range(n):
            if i == k or j == k:
                continue
            a,b = xy[i]
            c,d = xy[j]
            e,f = xy[k]
            if (d-b)*(e-a) == (c-a)*(f-b):
                print("Yes")
                exit()
print("No")