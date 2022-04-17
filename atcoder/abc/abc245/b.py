n = int(input())
num = [0]*(2005)
for a in map(int,input().split()):
    num[a] += 1

for i in range(2005):
    if num[i] == 0:
        print(i)
        exit()