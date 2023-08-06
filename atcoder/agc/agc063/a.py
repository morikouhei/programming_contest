n = int(input())
S = input()

num = [0,0]
if S[0] == "A":
    num[0] += 1
else:
    num[1] += 1
ans = []
for i in range(1,n+1):
    if S[i] == "A":
        num[0] += 1
    else:
        num[1] += 1

    
    if i%2:
        # Alice
        bob = i//2
        if num[0] <= bob:
            ans.append("Bob")
        else:
            ans.append("Alice")
    else:
        alice = i//2
        if num[1] <= alice:
            ans.append("Alice")
        else:
            ans.append("Bob")

for i in ans:
    print(i)