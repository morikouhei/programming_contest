from collections import Counter
n,m = map(int,input().split())
A = list(map(int,input().split()))

C = Counter([a%m for a in A])
for key,value in C.items():
    if value%2:
        print("Alice")
        exit()
print("Bob")
