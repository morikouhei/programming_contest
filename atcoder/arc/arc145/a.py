n = int(input())
S = input()
if S == S[::-1]:
    print("Yes")
    exit()

if len(S) == 2:
    print("No")
    exit()

if S[0] == "B" or S[-1] == "A":
    print("Yes")
    exit()

l = 0
r = n-1
while l < r:
    if S[l] == "A" and S[r] == "B":
        print("No")
        exit()
    if S[l] == "B" or S[r] == "A":
        print("Yes")
        exit()
    l += 1
    r -= 1
print("Yes")