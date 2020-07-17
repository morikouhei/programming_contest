t = int(input())

for i in range(t):
    l = [list(input()) for i in range(9)]
    
    for k in range(9):
        for j in range(9):
            if l[k][j] == "1":
                l[k][j] ="2"
        
    for k in l:
        print(*k,sep="")
