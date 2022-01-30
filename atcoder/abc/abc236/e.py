import sys
input = sys.stdin.readline

def main():
    n = int(input())
    A = list(map(int,input().split()))
    inf = 10**20
    def average(x):
        dp = [-inf]*2
        dp[0] = 0

        for a in A:
            now = a-x
            ndp = [-inf]*2
            ndp[0] = max(dp[0],dp[1])+now
            ndp[1] = dp[0]
            dp = ndp
        return max(dp)




    l = 0
    r = 10**9+5
    for i in range(40):
        m = (r+l)/2
        if average(m) >= 0:
            l = m
        else:
            r = m
    print(l)


    def median(x):
        count = 0
        last = -1
        less = 0
        for i,a in enumerate(A):
            if a >= x:
                less += (i-last-1)//2
                last = i
                count += 1
        less += (n-last-1)//2
        return count > less

    l = 0
    r = 10**9+5
    while r > l + 1:
        m = (r+l)//2
        if median(m):
            l = m
        else:
            r = m
    print(l)

if __name__ == "__main__":
    main()