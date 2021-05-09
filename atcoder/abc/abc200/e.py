n,k = map(int,input().split())

l = 3
r = 3*n+1
L = [1,3,3,1]
L2 = [1,2,1]
def calc(x):
    base = 0
    for i in range(3):
        now = x-n*i
        if now < 0:
            break
        base += ((-1)**i)*(now*(now-1)*(now-2))//6*L[i]
    return base


def calc2(x,num):
    base = 0
    for i in range(3):
        now = num-x-2-n*i+1
        if now < 0:
            break
        base += ((-1)**i)*now*L2[i]
    return base
    
while r > l + 1:
    m = (r+l)//2
    if calc(m) <= k:
        l = m
    else:
        r = m
if calc(l) == k:
    ans = [1,1,1]
    l -= 3
    now = 0
    while l:
        if l >= n-1:
            ans[now] = n
            l -= n-1
            now += 1
        else:
            ans[now] += l
            l = 0
    print(*ans)
    exit()
k -= calc(l)
num = r

for i in range(1,n+1):
    x = calc2(i,num)
    if x < k:
        k -= x
    else:
        ans1 = i
        left = num-i
        if left <= n+1:
            ans2 = k
            ans3 = left -ans2
        else:
            ans3 = n-k+1
            ans2 = left-ans3
        print(ans1,ans2,ans3)
        exit()

