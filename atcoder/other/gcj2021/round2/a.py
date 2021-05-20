import sys

def solve():
    for i in range(1,n):
        print("M",i,n)
        sys.stdout.flush()
        x = int(input())
        if x == i:
            continue
        print("S",i,x)
        sys.stdout.flush()
        int(input())
    print("D")
    sys.stdout.flush()
    int(input())
T,n = map(int,input().split())
for t in range(T):
    ans = solve()
