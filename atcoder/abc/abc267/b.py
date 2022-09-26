S = input()
S = [int(s) for s in S]
if S[0] == 1:
    print("No")
    exit()
Lane = [0]*7
Lane[0] = S[6]
Lane[1] = S[3]
Lane[2] = S[7]+S[1]
Lane[3] = S[4]+S[0]
Lane[4] = S[8]+S[2]
Lane[5] = S[5]
Lane[6] = S[9]
for i in range(7):
    if Lane[i] == 0:
        continue
    for j in range(i+1,7):
        if Lane[j]:
            if j > i+1:
                print("Yes")
                exit()
            break
print("No")