s = input()
count = 0
MAX = 0
for i in s:
    if i == "(":
        count += 1
        MAX = max(count,MAX)
    elif i == ")":
        count -= 1

for i in range(MAX,0,-1):
    c = ""
    count = 0
    now = 0
    while now < len(s):
        if s[now] == "(":
            count += 1
            if count < i:
                c += "("
            else:
                k = ""
                now += 1
                while s[now] != ")":
                    k += s[now]
                    now += 1
                k += k[::-1]
                count -= 1
                c += k
        elif s[now] == ")":
            count -= 1
            c += ")"
        else:
            c += s[now]
        now += 1
    s = c
print(s)