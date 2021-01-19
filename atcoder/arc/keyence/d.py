n = int(input())
print(2**n-1)

for i in range(1,2**n):
    c = ""
    for j in range(1,2**n+1):
        if bin(i&j).count("1")%2:
            c += "A"
        else:
            c += "B"
    print(c)
