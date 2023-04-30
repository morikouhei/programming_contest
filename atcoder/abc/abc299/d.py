import sys

n = int(input())

l = 1
r = n


def query(m):
    print("?",m)
    sys.stdout.flush()
    return int(input())



while r > l + 1:
    m = (r+l)//2

    if query(m):
        r = m
    else:
        l = m

print("!",l)
sys.stdout.flush()