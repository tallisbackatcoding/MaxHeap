#Binary Indexed/Fenwick Tree
class BIT:
    def __init__(self, arr):
        prefixSum = [0]
        for i in range(len(arr)):
            prefixSum.append(prefixSum[-1]+arr[i])
        self.arr = [0] * (len(arr)+1)
        for i in range(1, len(self.arr)):
            bottom = i & -i
            self.arr[i] = prefixSum[i] - prefixSum[i-bottom]

    def sum(self, i):
        i+=1
        ans = 0
        while i != 0:
            ans += self.arr[i]
            i &= i - 1 
        return ans
    def rangeSum(self, l, r):
        return self.getSum(r) - self.getSum(l-1)
    def add(self, i, val):
        i+=1
        while i < len(self.arr):
            self.arr[i] += val
            i += i & -i
