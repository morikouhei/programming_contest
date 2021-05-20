n = int(input())
S = [input().split() for i in range(n)]
L = [[int(S[i][1]),i] for i in range(n)]
L.sort(reverse=True)
print(S[L[1][1]][0])