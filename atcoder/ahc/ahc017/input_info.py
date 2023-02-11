import glob
import os
import pandas as pd
### change ahc xxx to current contest 

base_path = "/Users/morikouhei/github/programming_contest/atcoder/ahc/ahc017"
input_files_path = os.path.join(base_path,"tools_3/in/*.txt")
files = glob.glob(input_files_path)

dic = {}
for file in files:
     with open(file,"r") as f:
        n,m,d,k = [int(x) for x in f.readline().split()]
        if n not in dic:
            dic[n] = [m,m,0]
        dic[n][0] = min(dic[n][0],m)
        dic[n][1] = max(dic[n][1],m)
        dic[n][2] += 1

print(len(dic))

l = []
for key in sorted(dic.keys()):
    mi,ma,nums = dic[key]
    l.append([key,mi,mi/key,ma,ma/key,nums])

df = pd.DataFrame(l,columns=["N","min of M","ratio of min M / N","max of M","ratio of max M / N","nums"])

file_out_path = os.path.join(base_path,"stats/input_parameter.xlsx")

df.to_excel(file_out_path)