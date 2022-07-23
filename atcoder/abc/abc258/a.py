k = int(input())
if k < 60:
    print("21:"+str(k).zfill(2))
else:
    print("22:"+str(k-60).zfill(2))