n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


# 非クラス版
base = 3*10**5+7; mod = 10**9 + 9

def rolling_hash(s):
    l = len(s)
    h = [0]*(l + 1)
    lis = set()

    for i in range(l):
        s1 = s[i]
        if s1 in lis:
            h[i+1] = h[i]
        else:
            h[i+1] = (h[i]+pow(base,s1,mod)) % mod
        lis.add(s1)
    return h

Ahash = rolling_hash(A)
Bhash = rolling_hash(B)
q = int(input())
for _ in range(q):
    x,y = map(int,input().split())
    print("Yes" if Ahash[x] == Bhash[y] else "No")
