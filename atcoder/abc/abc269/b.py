S = [input() for i in range(10)]
n = 10
a = -1
c = -1

for i in range(n):
    for j in range(n):
        if S[i][j] == "#":
            if a == -1:
                a = i+1
                c = j+1
            b = i+1
            d = j+1

print(a,b)
print(c,d)
