n = int(input())
A = list(map(int,input().split()))
need,m = divmod(sum(A),10)
if m:
    print("No")
    exit()
s = set()
s.add(0)
cum = 0
for i in A+A:
    cum += i
    if cum-need in s:
        print("Yes")
        exit()
    s.add(cum)
print("No")

