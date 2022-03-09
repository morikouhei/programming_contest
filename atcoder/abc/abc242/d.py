S = input()

dic = {"A":"BC","B":"CA","C":"AB"}
l = "ABC"
def solve():
    T,k = map(int,input().split())
    t = min(T,70)
    if t == 0:
        return S[k-1]

    p2 = pow(2,t)
    k -= 1
    ind = (k)//p2
    now = S[ind]
    k %= p2

    for i in range(t)[::-1]:
        p2 = pow(2,i)

        if k >= p2:
            k -= p2
            now = dic[now][1]
        else:
            now = dic[now][0]
    
    if t < T:
        dif = (T-t)%3
        ind = l.index(now)
        ind += dif
        now = l[ind%3]

    return now



q = int(input())
for _ in range(q):
    print(solve())