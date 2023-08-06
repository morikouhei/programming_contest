from heapq import heappush,heappop
import sys
input = sys.stdin.readline

n = int(input())
AB = [list(map(int,input().split())) for i in range(n)]

score = 0

h = []

for a,b in AB:
    heappush(h,[b-a,a])

for i in range(n):

    ba,a = heappop(h)

    heappush(h,[-ba,a+ba])

    ba,a = heappop(h)

    score += a
print(score)