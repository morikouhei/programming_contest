n,m = map(int,input().split())
PCF = []

for i in range(n):
    p,c,*f = map(int,input().split())
    PCF.append([p,c,set(f)])

for i in range(n):
    for j in range(n):

        if PCF[i][0] >= PCF[j][0] and (PCF[i][2] & PCF[j][2]) == PCF[i][2] and (PCF[i][0] > PCF[j][0] or len(PCF[i][2]) < len(PCF[j][2])):
            print("Yes")
            exit()
print("No")