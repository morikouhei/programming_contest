n,k = map(int,input().split())

def change8_10(x):
    count = 0
    for i in str(x):
        count *= 8
        count += int(i)
    return count

def change10_9(x):
    num = ""
    now= x
    while now:
        now,m = divmod(now,9)
        num += str(m)
    if num == "":
        num = "0"
    return int(num[::-1])

def change5(x):
    num = ""
    for i in str(x):
        if i == "8":
            num += "5"
        else:
            num += i
    return num

for i in range(k):
    n = change5(change10_9(change8_10(n)))
print(n)