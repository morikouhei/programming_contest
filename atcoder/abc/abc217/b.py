S = [input() for i in range(3)]
L = ["ABC" , "ARC" , "AGC" , "AHC"]
for l in L:
    if l in S:
        continue
    print(l)
