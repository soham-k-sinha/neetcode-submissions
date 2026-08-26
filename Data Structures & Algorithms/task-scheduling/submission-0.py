class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [-i for (l, i) in collections.Counter(tasks).items()] # O(n)
        heapq.heapify(count) # O(26)
        queue = deque([])
        time = 0

        while count or queue:
            task = heapq.heappop(count) if count else None
            time += 1
            if task and task != -1:
                queue.append((task + 1, time + n))
            if queue and queue[0][1] == time:
                val = queue.popleft()[0]
                heapq.heappush(count, val)

        return time