n = int(input())
s = list(input())
k = int(input())
t = s[k]
for i in range(n):
    if s[i] != t:
        s[i] = "*"
print(*s,sep="")