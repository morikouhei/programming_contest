n = int(input())
S = [input() for i in range(n)]

for i in range(n):
    for j in range(n):
        if j+6 <= n:
            w = 0
            for k in range(6):
                if S[i][j+k] == ".":
                    w += 1
            if w <= 2:
                print("Yes")
                exit()
        if i+6 <= n:
            w = 0
            for k in range(6):
                if S[i+k][j] == ".":
                    w += 1
            if w <= 2:
                print("Yes")
                exit()
        if i+6 <= n and j+6 <= n:
            w = 0
            for k in range(6):
                if S[i+k][j+k] == ".":
                    w += 1
            if w <= 2:
                print("Yes")
                exit()

        if i+6 <= n and j-5 >= 0:
            w = 0
            for k in range(6):
                if S[i+k][j-k] == ".":
                    w += 1
            if w <= 2:
                print("Yes")
                exit()

print("No")
