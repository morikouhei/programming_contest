n = int(input())
S = set()

for i in range(n):
    s = input()
    S.add(min(s,s[::-1]))
print(len(S))