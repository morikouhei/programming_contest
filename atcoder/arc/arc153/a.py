n = int(input())

def get(x):
    x = str(x)
    s = x[0]+x[0]+x[1]+x[2]+x[3]+x[3]+x[4]+x[5]+x[4]
    return int(s)

print(get(10**5+n-1))