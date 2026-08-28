class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if not self.arr:
            self.arr.append(num)
            return
        
        # O(log n)
        l, r = 0, len(self.arr)

        while l < r:
            m = (l+r)//2

            if self.arr[m] < num:
                l = m + 1
            else:
                r = m
        
        # O(n)
        self.arr.insert(l, num)


    def findMedian(self) -> float:
        if len(self.arr) % 2 == 0:
            midR = int(len(self.arr) / 2)
            midL = midR - 1
            return (self.arr[midL] + self.arr[midR]) / 2.0
        
        mid = len(self.arr) // 2
        return float(self.arr[mid])
        
        