n = int(input())
S = [input() for i in range(n)]
print("Yes" if S.count("For") > n//2 else "No")