def solve():
       
   return
    

                    

            

t = int(input())
for i in range(t):
    ans = solve()
    print("Case #{}:".format(i+1),end=" ")
    if ans == "IMPOSSIBLE":
        print(ans)
        continue
    print("POSSIBLE")
    for i in ans:
        print(*i)
    
