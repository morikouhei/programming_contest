n = int(input())
A = [input() for i in range(n)]
for i in range(n):
    for j in range(i):
        if A[i][j] == "D" and A[j][i] != "D":
            print("incorrect")
            exit()

        if A[i][j] == "W":
            if A[j][i] != "L":
                print("incorrect")
                exit()

        if A[i][j] == "L":
            if A[j][i] != "W":
                print("incorrect")
                exit()

print("correct")