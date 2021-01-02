a,b = input().split()
s = sum([int(i) for i in a])
x = sum([int(i) for i in b])
print(max(s,x))