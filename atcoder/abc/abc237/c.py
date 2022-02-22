S = list(input())

n = len(S)
l = 0
r = n-1

while True:
    if l >= r:
        print("Yes")
        exit()

    if S[r] == S[l]:
        l += 1
        r -= 1
    else:
        if S[r] == "a":
            r -= 1
        else:
            break

print("No")