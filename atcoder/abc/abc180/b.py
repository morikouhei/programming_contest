n = int(input())
x = list(map(int,input().split()))
a = b = c = 0

for i in x:
    a += abs(i)
    b += i**2
    c = max(c,abs(i))
b = b**0.5
for i in (a,b,c):
    print(i)