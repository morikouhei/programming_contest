n = int(input())
s = set()
for i in range(n):
    a = input()
    if a in s:
        continue
    s.add(a)
    print(i+1)