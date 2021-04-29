
def calc_time(a,b,c):
    hour,mod_hour = divmod(a,(10**9)*60*60)
    minute,mod_minute = divmod(b,(10**9)*12*60)
    second,mod_second = divmod(c,(10**9)*12*60)
    ans = [hour,minute, second, mod_second]
    if mod_hour == minute*10**9*60+second*10**9+mod_second:
        return ans
    return -1
    
p = 12*(10**10)
def solve():
    a,b,c = map(int,input().split())
    mi = min(a,b,c)
    a -= mi
    b -= mi
    c -= mi
    ans = calc_time(a,b,c)
    if ans != -1:
        return ans
    ans = calc_time(b,a,c)
    if ans != -1:
        return ans
    ans = calc_time(c,b,a)
    if ans != -1:
        return ans
    ans = calc_time(a,c,b)
    if ans != -1:
        return ans
    ans = calc_time(b,c,a)
    if ans != -1:
        return ans
    ans = calc_time(c,a,b)
    if ans != -1:
        return ans

    return [-1]


T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: ".format(t+1),end="")
    print(*ans)