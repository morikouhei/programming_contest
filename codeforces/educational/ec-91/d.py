n,m = map(int,input().split())
x,k,y = map(int,input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

if n == m:
    if a == b:
        print(0)
    else:
        print(-1)
    exit()
now = 0
l = [-1]
for i in range(n):
    if b[now] == a[i]:
        l.append(i)
        now += 1
        if now == m:
            break
l.append(n)
if now != m:
    print(-1)
    exit()
ans = 0
for q in range(1,len(l)):
    w = l[q]-l[q-1]-1
    if w <= 0:
        continue
    if w < k:
        if l[q] < n:
            c1 = a[l[q]]
        else:
            c1 = 0
        if l[q-1] == -1:
            c2 = 0
        else:
            c2 = a[l[q-1]]
        if max(a[max(0,l[q-1]):l[q]]) > max(c1,c2):
            print(-1)
            exit()
        else:
            ans += y*w
    else:
        if x <= y*k:
            ans += x*(w//k)+y*(w%k)
        else:
            if l[q] < n:
                c1 = a[l[q]]
            else:
                c1 = 0
            if l[q-1] == -1:
                c2 = 0
            else:
                c2 = a[l[q-1]]
            if max(a[max(0,l[q-1]):l[q]]) > max(c1,c2):
                ans += x + y*(w-k)
            else:
                ans += y*w
print(ans)
