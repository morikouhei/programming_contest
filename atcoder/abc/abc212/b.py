s = input()
a = int(s[0])
b = int(s[1])
c = int(s[2])
d = int(s[3])
if a == b == c == d:
    print("Weak")
    exit()
if (a+1)%10 == b and (b+1)%10 == c and (c+1)%10 == d:
    print("Weak")
else:
    print("Strong")