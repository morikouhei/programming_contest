s = input()

s = s[::-1]
n = len(s)
ans = 0
bef = 0
count = [0]*26
for i in range(n-1):
    if s[i] == s[i+1]:
        x = ord(s[i])-ord("a")
        ans += i-count[x]
        for j in range(26):
            count[j] = 0
        count[x] = i+1
    else:
        x = ord(s[i])-ord("a")
        count[x] += 1
print(ans)
