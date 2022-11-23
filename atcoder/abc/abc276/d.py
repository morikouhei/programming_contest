n = int(input())
A = list(map(int,input().split()))

twos = [0]*n
threes = [0]*n
for i in range(n):
    a = A[i]
    while a % 2 == 0:
        a //= 2
        twos[i] += 1
    while a % 3 == 0:
        a //= 3
        threes[i] += 1

    A[i] = a

if len(set(A)) != 1:
    print(-1)
    exit()

cost = sum(twos) - min(twos)*n
cost += sum(threes) - min(threes)*n
print(cost)