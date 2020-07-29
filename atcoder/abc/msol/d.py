n = int(input())
a = list(map(int,input().split()))

count = [1000,0]
x = a[0]
for i in range(1,n):
    if a[i] > x:
        d = count[0]//x
        count = [count[0]-d*x, d+count[1]]
    else:
        count = [count[0]+count[1]*x,0]
    x = a[i]
if count[1]:
    count[0] += count[1]*x
print(count[0])