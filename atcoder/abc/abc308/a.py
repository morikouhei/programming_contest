S = list(map(int,input().split()))

if sorted(S) != S:
    print("No")
else:
    for x in S:
        if x%25 or x < 100 or x > 675:
            print("No")
            exit()
    print("Yes")