s = input()
for i in range(len(s)):
    if i%2 and s[i].upper() != s[i]:
        print("No")
        exit()
    if i%2==0 and s[i].upper() == s[i]:
        print("No")
        exit()
print("Yes")