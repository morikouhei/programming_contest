x = int(input())
M = int(input())

ma = 0
for i in str(x):
    ma = max(ma,int(i))
if len(str(x)) == 1:
    if M >= ma:
        print(1)
    else:
        print(0)
    exit()
l = ma
r = 10**20

while r - l > 1:
    m = (r+l)//2
    now = 0
    for i in str(x):
        now *= m
        now += int(i)
    if now > M:
        r = m
    else:
        l = m
print(l-ma)