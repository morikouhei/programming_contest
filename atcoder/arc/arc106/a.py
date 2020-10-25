n = int(input())
for i in range(1,100):
    for j in range(1,100):
        if 5**i + 3**j == n:
            print(j,i)
            exit()

print(-1)