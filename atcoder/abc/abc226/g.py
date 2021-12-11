def solve():
    A = [0]+list(map(int,input().split()))
    B = [0]+list(map(int,input().split()))

    for i in range(6):
        if B[i] >= A[i]:
            B[i] -= A[i]
            A[i] = 0
        else:
            A[i] -= B[i]
            B[i] = 0

    
    if A[5]:
        return "No"

    if A[4]:
        if A[4] > B[4]+B[5]:
            return "No"
        B[5] -= A[4]
        B[1] += A[4]

    if A[3]:
        if A[3] > B[3]+B[4]+B[5]:
            return "No"
        if A[3] <= B[5]:
            B[5] -= A[3]
            B[2] += A[3]
        else:
            A[3] -= B[5]
            B[2] += B[5]
            B[5] = 0
            B[4] -= A[3]
            B[1] += A[3]

    if A[2]:
        if A[2] > B[2]+B[3]+B[4]*2+B[5]*2:
            return "No"

        B[2] += B[3]+B[4]*2+B[5]*2
        B[1] += B[3]+B[5]
        B[3] = B[4] = B[5] = 0
        B[2] -= A[2]
 
    if A[1] > B[1]+B[2]*2+B[3]*3+B[4]*4+B[5]*5:
        return "No"

    return "Yes"

            
    

t = int(input())
for _ in range(t):
    print(solve())