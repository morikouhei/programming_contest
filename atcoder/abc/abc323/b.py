n = int(input())
wins = []
for i in range(n):
    s = input()
    wins.append([-s.count("o"),i+1])
wins.sort()
ans = [ind for _,ind in wins]
print(*ans)