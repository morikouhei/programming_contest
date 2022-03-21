n = int(input())
A = list(map(int,input().split()))

if A[-2]+1 < A[-1]:
    print("Alice")
else:
    print("Alice" if (A[-1]-n+1)%2 else "Bob")