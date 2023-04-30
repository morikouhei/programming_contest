n = int(input())
S = input()
for i in range(1,n):
    if S[i-1] == S[i]:
        print("No")
        exit()
print("Yes")