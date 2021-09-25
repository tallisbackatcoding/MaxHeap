class MaxHeap:
    def __init__(self):
        self.arr = [-1]
        self.size = 0
    def p(self, i):
        idx = i >> 1
        if idx < 1:
            return None
        return idx
    def r(self, i):
        idx = (i << 1) + 1
        if idx > self.size:
            return None
        return idx
    def l(self, i):
        idx =  i << 1
        if idx > self.size:
            return None
        return idx
    def shiftUp(self, i):
        if self.p(i) == None:
            return
        if self.arr[self.p(i)] < self.arr[i]:
            self.arr[self.p(i)], self.arr[i] = self.arr[i], self.arr[self.p(i)]
            self.shiftUp(self.p(i))
    def max_(self, a, b):
        if a == None and b == None:
            return None
        if a == None:
            return b
        if b == None:
            return a
        if self.arr[a] < self.arr[b]:
            return b
        return a

    def shiftDown(self, i):
        idx = self.max_(self.l(i), self.r(i))
        if idx != None:
            self.arr[idx], self.arr[i] = self.arr[i], self.arr[idx]
            self.shiftDown(idx)
    def insert(self, val):
        self.size += 1
        self.arr.append(val)
        self.shiftUp(self.size)
    def peek(self):
        if self.size < 1:
            return None
        return self.arr[1]
    def pop(self):
        if self.size < 1:
            return None
        val = self.arr[1]
        self.arr[1], self.arr[self.size] = self.arr[self.size], self.arr[1]
        self.arr.pop()
        self.size -= 1
        self.shiftDown(1)
        return val

pq = MaxHeap()


