L = ["H" , "2B" , "3B" , "HR"]
S = [input() for i in range(4)]
for l in L:
    if l not in S:
        print("No")
        exit()
print("Yes")