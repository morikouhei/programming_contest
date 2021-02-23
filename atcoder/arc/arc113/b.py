a,b,c = map(int,input().split())
now = a
l = []
while True:
    if now%10 in l:
        break
    l.append(now%10)
    now *= a
    now %= 10

n = len(l)
b = pow(b,c,n)
print(l[b-1])
