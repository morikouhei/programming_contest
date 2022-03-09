from collections import Counter
n,m = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ca = Counter(A)
cb = Counter(B)
for k,v in cb.items():
    if k in ca and v <= ca[k]:
        continue
    print("No")
    exit()
print("Yes")