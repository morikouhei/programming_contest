n,q = map(int,input().split())
S = input()
now = 0
for _ in range(q):
    t,x = map(int,input().split())
    if t == 1:
        now -= x
        now %= n
    else:
        print(S[(now+x-1)%n])