n = str(input())

for i in range(20):
    s = "0"*i + n
    if s == s[::-1]:
        print("Yes")
        exit()
print("No")