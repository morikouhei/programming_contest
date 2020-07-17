t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if "10" not in s:
        print(s)
    elif s[0] == "0":
        if s[-1] == "1":
            ans = ""
            for i in range(n):
                if s[i] == "0":
                    ans += "0"
                else:
                    break
            ans += "0"
            for i in range(n-1,-1,-1):
                if s[i] == "1":
                    ans += "1"
                else:
                    break
            print(ans)
        else:
            ans = ""
            for i in range(n):
                if s[i] == "0":
                    ans += "0"
                else:
                    break
            ans += "0"
            print(ans)
    else:
        ans ="0"
        for i in range(n-1,-1,-1):
            if s[i] == "1":
                ans += "1"
            else:
                break
        print(ans)

