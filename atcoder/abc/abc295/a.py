n = int(input())
W = input().split()
s = ["and","not","that","the","you"]
for w in W:
    if w in s:
        print("Yes")
        exit()
print("No")