h,w = map(int,input().split())
R = list(map(int,input().split()))
C = list(map(int,input().split()))
A = [list(map(int,input())) for i in range(h)]

M = h*w
inf = 10**15
dp = [inf]*(4*M)

dp[0] = 0
dp[1] = R[0]
dp[2] = C[0]
dp[3] = R[0]+C[0]
for i in range(h):
    for j in range(w):
        for ch in range(2):
            for cw in range(2):
                num = dp[(i*w+j)*4 + ch + cw*2]
                c = A[i][j]

                if i < h-1:
                    nc = 0 if (c+ch)%2 == A[i+1][j] else 1
                    nid = ((i+1)*w+j)*4 + cw*2 + nc
                    dp[nid] = min(dp[nid],num+nc*R[i+1])

                if j < w-1:
                    nc = 0 if (c+cw)%2 == A[i][j+1] else 1
                    nid = (i*w+j+1)*4 + ch + nc*2
                    dp[nid] = min(dp[nid],num+nc*C[j+1])

print(min(dp[-4:]))
