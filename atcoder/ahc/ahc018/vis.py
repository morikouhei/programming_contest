import numpy as np
import matplotlib.pyplot as plt
import random


# nums = [i for i in range(10001)]
# count = [0]*10001
mi = -1000
ma = 1000
hist_dx = [[0]*2001 for i in range(10)]
hist_dy = [[0]*2001 for i in range(10)]
N = 200
for i in range(1000):
    in_txt = f"/Users/morikouhei/Downloads/tools/in/{str(i).zfill(4)}.txt"

    with open(in_txt,"r") as f:
        n,w,k,c = [int(x) for x in f.readline().split()]
        data = [[int(x) for x in f.readline().split()] for i in range(n)]

        # for x in data:
        #     for y in x:
        #         count[y] += 1
        
        for X in data:
            for x,nx in zip(X,X[1:]):
                hist_dx[x//501][nx-x+1000] += 1
        for i in range(N-1):
            for j in range(N):
                y,ny = data[i][j],data[i+1][j]
                hist_dy[y//501][ny-y+1000] += 1



nums = [i for i in range(-1000,1001)]
# dX = []
# for X in data:
#     l = []
#     for x,nx in zip(X,X[1:]):
#         l.append(nx-x)
#     dX.append(l)
# dY = []
# for i in range(N-1):
#     l = []
#     for j in range(N):
#         y,ny = data[i][j],data[i+1][j]
#         l.append(ny-y)
#     dY.append(l)

# dX = np.array(dX)
# dY = np.array(dY)
# data = np.array(data)
fig = plt.figure()
# ax = fig.add_subplot(1,2,1)
# im = ax.imshow(data, origin='lower')
# plt.colorbar(im)
for i in range(10):
    ax = fig.add_subplot(5,4,2*i+1)
    ax.bar(nums,hist_dx[i])

    ax = fig.add_subplot(5,4,2*i+2)
    ax.bar(nums,hist_dy[i])
    print(sum(hist_dx[i]),sum(hist_dy[i]))
# ax = fig.add_subplot(2,5,1)
# ax.bar(nums,hist_dx)
# im = ax.imshow(dX, origin='lower')
# plt.colorbar(im)

# ax = fig.add_subplot(2,2,3)
# im = ax.imshow(dY, origin='lower')
# plt.colorbar(im)
# # plt.show()


# nums = [i for i in range(-1000,1001)]
# # count = [0]*
# # for x in hist:
# #     count[x//50] += 1
# # data = np.array(hist)
# ax = fig.add_subplot(2,2,2)
# # ax.hist(data, bins=500, histtype='barstacked', ec='black')
# # ax.set_ylim(0,10000)
# ax.bar(nums,hist_dx)


# ax = fig.add_subplot(2,2,4)
# # ax.hist(data, bins=500, histtype='barstacked', ec='black')
# # ax.set_ylim(0,10000)
# ax.bar(nums,hist_dy)
plt.show()