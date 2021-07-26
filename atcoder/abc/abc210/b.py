n = int(input())
S = input()
for i in range(n):
    s = S[i]
    if s == "1":
        if i%2:
            print("Aoki")
        else:
            print("Takahashi")
        exit()