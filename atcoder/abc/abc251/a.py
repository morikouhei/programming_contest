S = input()
for i in range(1,7):
    s = S*i
    if len(s) == 6:
        print(s)
        exit()