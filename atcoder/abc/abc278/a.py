n,k = map(int,input().split())
A = list(map(int,input().split()))[k:]+[0]*k

print(*A[-n:])