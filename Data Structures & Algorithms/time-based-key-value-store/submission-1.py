class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        
        self.hashmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        lis = self.hashmap.get(key, []) # [[val, timestamp]]
        l, r = 0, len(lis) - 1
        while l <= r:
            m = l + ((r-l) // 2)
            if timestamp == lis[m][1]:
                return lis[m][0]
            elif timestamp > lis[m][1]:
                res = lis[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
        
