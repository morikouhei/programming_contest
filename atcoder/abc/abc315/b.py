m = int(input())
D = list(map(int,input().split()))

s = sum(D)//2 + 1

for i,d in enumerate(D):
    if d < s:
        s -= d
    else:
        print(i+1,s)
        exit()