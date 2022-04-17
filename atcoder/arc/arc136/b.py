from collections import Counter

n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))


def swap(i):
    A[i],A[i+1],A[i+2] = A[i+2],A[i],A[i+1]



if Counter(A) != Counter(B):
    print("No")
    exit()


for i in range(n-3):
    if A[i] == B[i]:
        continue

    for j in range(i+1,n):
        if A[j] == B[i]:
            start = j
            break
    
    while A[i] != B[i]:
        if start - i > 2:
            start -= 2
            swap(start)
        else:
            swap(i)

for i in range(3):

    check = 1
    for j in range(3):
        if A[-1-j] != B[-1-j]:
            check = 0
    if check:
        print("Yes")
        exit()
    swap(n-3)

for v in Counter(A).values():
    if v > 1:
        print("Yes")
        exit()
print("No")
