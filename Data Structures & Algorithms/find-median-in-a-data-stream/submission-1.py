class MedianFinder:

    def __init__(self):
        self.smallHeap = [] # MaxHeap
        self.largeHeap = [] # MinHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.smallHeap, -num)
        
        if (self.smallHeap and self.largeHeap and -self.smallHeap[0] > self.largeHeap[0]):
            el = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, el)
        
        if len(self.smallHeap) - len(self.largeHeap) > 1:
            el = -heapq.heappop(self.smallHeap)
            heapq.heappush(self.largeHeap, el)
        if len(self.largeHeap) - len(self.smallHeap) > 1:
            el = -heapq.heappop(self.largeHeap)
            heapq.heappush(self.smallHeap, el)

    def findMedian(self) -> float:
        if len(self.smallHeap) > len(self.largeHeap):
            return -self.smallHeap[0]
        elif len(self.smallHeap) < len(self.largeHeap):
            return self.largeHeap[0]
        else:
            return (-self.smallHeap[0] + self.largeHeap[0]) / 2.0
        
        