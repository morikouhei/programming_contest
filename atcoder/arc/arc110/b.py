n = int(input())
t = input()
s = "110"*(n//3+10)
if t not in s:
    print(0)
    exit()
if t == "1":
    print(2*10**10)
    exit()
if t == "11":
    print(10**10)
    exit()
if s[:n] == t:
    x = (n-1)//3
    print(10**10-x)
    exit()
elif s[1:n+1] == t:
    x = n//3
    print(10**10-x)
    exit()
x = (n+1)//3
print(10**10-x)