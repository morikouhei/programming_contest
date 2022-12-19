S = input()
if len(S) != 8:
    print("No")
    exit()

nums = [str(i) for i in range(10)]

if "A" <= S[0] <= "Z" and "A" <= S[-1] <= "Z":
    for i in S[1:-1]:
        if i not in nums:
            print("No")
            exit()
    if int(S[1]) > 0:
        print("Yes")
        exit()
print("No")