n = int(input())
S = [input() for i in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x = S[i]+S[j]
        if x == x[::-1]:
            print("Yes")
            exit()
print("No")