N = int(input())
S = input()
count = 0

li = ["a","a","a"]
for i in S:
    li.append(i)
    if li[-3:] == ["f","o","x"]:
        for k in range(3):
            li.pop()
print(len(li)-3)