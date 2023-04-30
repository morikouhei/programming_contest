def calc_b(n,b):
    while n:
        n,m = divmod(n,b)
        if m > 1:
            return 0
    return 1


def search_b(x,bit):

    num = 0
    now = 1
    for j in range(6):
        if bit >> j & 1:
            num += now
        now *= x
    return num

def binary_search(n,bit):

    l = 1001
    r = n+1

    while r > l + 1:
        m = (r+l)//2
        if search_b(m,bit) <= n:
            l = m
        else:
            r = m

    if search_b(l,bit) == n:
        return 1
    return 0
def solve():
    n = int(input())
    ans = 0
    for i in range(2,min(1000,n)+1):
        ans += calc_b(n,i)

    for bit in range(1,1<<6):
        ans += binary_search(n,bit)

    return ans
t = int(input())

for _ in range(t):
    print(solve())