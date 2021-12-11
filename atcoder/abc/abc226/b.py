n = int(input())
l = [tuple(map(int,input().split())) for i in range(n)]
print(len(set(l)))