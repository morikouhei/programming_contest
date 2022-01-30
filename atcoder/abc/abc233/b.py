l,r = map(int,input().split())
S = list(input())
S2 = S[:]
S2[l-1:r] = S2[l-1:r][::-1]
print(*S2,sep="") 