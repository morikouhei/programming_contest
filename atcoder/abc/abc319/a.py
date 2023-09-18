S = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481"""

base = S.split("\n")

s = input()
for x in base:
    if x.startswith(s):
        print(x.split()[1])