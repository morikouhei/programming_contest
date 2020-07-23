import copy
t = int(input())
c = list("abacaba")
for _ in range(t):
    n = int(input())
    s = list(input())
    check = False
    for i in range(n-6):
        check2 = True
        for j in range(7):
            if s[i+j] == c[j] or s[i+j] == "?":
                continue
            else:  
                check2 = False
                break
        if check2:
            s2 = copy.deepcopy(s)
            for j in range(7):
                s2[i+j] = c[j]
            count = 0

            for k in range(n-6):
                check2 = True
                
                for t in range(7):
                    if s2[k+t] == c[t]:
                        continue
                    else:
                        check2 = False
                        break  
                if check2:
                    count += 1
            if count == 1:
                for j in range(n):
                    if s2[j] == "?":
                        s2[j] = "z"
                print("Yes")
                print(*s2,sep="")
                check = True
        if check:
            break
    if check:
        continue
    print("No") 

    

                
