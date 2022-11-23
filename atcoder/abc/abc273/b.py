x,k = map(int,input().split())

ten = 1
for i in range(k):
    ten *= 10
    m = x%ten
    x -= m
    if m*2 >= ten:
        x += ten
print(x)
