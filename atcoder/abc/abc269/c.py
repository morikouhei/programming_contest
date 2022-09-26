X = int(input())

l = []
for i in range(60):
    if X >> i & 1:
        l.append(1<<i)

for i in range(1<<len(l)):
    num = 0
    for j in range(len(l)):
        if i >> j & 1:
            num += l[j]
    print(num)