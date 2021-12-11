S = list(input())
s = len(set(S))
if s == 1:
    print(1)
elif s == 2:
    print(3)
else:
    print(6)