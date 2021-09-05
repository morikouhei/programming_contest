n = int(input())
L = [[input().split()] for i in range(n)]
for i in range(n):
    for j in range(i):
        if L[i] == L[j]:
            print("Yes")
            exit()
print("No")