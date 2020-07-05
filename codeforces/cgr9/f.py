import sys
l = list(map(int,input().split()))

print("First")
sys.stdout.flush()
x = max(l)*3-sum(l)
print(x)
sys.stdout.flush()
s = int(input())

if l.index(max(l))+1 != s:
    x = 2*max(l)-sum(l)+l[s-1]
    print(x)
    sys.stdout.flush()
    s = input()
    exit()
else:
    l[l.index(max(l))] += x
    x = max(l)*3-sum(l)
    print(x)
    sys.stdout.flush()
    s = int(input())
    if l.index(max(l))+1 != s:
        x = 2*max(l)-sum(l)+l[s-1]
        print(x)
        sys.stdout.flush()
        s = input()
        exit()
