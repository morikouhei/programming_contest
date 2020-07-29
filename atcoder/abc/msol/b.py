a,b,c = map(int,input().split())
k = int(input())

while k > 0:
    if b <= a:
        b *= 2
        k -= 1
    else:
        break
while k > 0:
    if c <= b:
        c *= 2
        k -= 1
    else:
        break
if a < b < c:
    print("Yes")
else:
    print("No")
