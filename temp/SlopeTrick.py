from heapq import *

class SlopeTrick():

    def __init__(self):
        self.L = []
        self.R = []
        self.shiftL = 0
        self.shiftR = 0
        self.min_f = 0

    # 関数に \__ 型の関数 max(0,a-x) を加算
    def addL(self, x):
        if self.R:
            dx = x-(self.R[0]+self.shiftR)
            self.min_f += max(0,dx)
        nx = heappushpop(self.R,x-self.shiftR)
        heappush(self.L,-(nx+self.shiftR-self.shiftL))

    # 関数に __/ 型の関数 max(0,x-a) を加算
    def addR(self, x):
        if self.L:
            dx = (-self.L[0]+self.shiftL)-x
            self.min_f += max(0,dx)
        nx = heappushpop(self.L,-(x-self.shiftL))
        heappush(self.R,-nx+self.shiftL-self.shiftR)

    # 関数に \/ 型の関数 max(a-x,x-a) を加算
    def addBoth(self,x):
        self.addL(x)
        self.addR(x)

    def addConst(self, x):
        self.min_f += x

    def sliding_window_minimum(self,left,right):
        self.L += left
        self.R += right

    def getmin(self):
        return self.min_f
