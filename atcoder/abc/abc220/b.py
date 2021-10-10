k = int(input())
a,b = input().split()
na = 0
nb = 0
for x in a:
    x = int(x)
    na *= k
    na += x

for x in b:
    x = int(x)
    nb *= k
    nb += x
print(na*nb)