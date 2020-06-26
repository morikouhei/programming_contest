n = int(input())
l = sorted(list(map(int,input().split())),reverse=True)
s = ""
for i in l:
    s += str(i)+" "
path_w = 'C:/Users/morik/test_w.txt'


with open(path_w, mode='w') as f:
    f.write(s)