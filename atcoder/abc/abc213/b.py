n = int(input())
A = list(map(int,input().split()))
sA = [[a,i] for i,a in enumerate(A)]
print(sorted(sA)[-2][1]+1)