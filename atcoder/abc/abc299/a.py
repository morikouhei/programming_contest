n = int(input())
S = input().replace(".","")
if S.find("|") < S.find("*") < S.rfind("|"):
    print("in")
else:
    print("out")