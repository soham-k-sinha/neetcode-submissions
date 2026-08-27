class Twitter:

    def __init__(self):
        # Hashmap to keep a track of posts
        # We need a stack for each id - latest posts are at the end
        self.posts = defaultdict(list)

        # Hashmap to keep a track of followers
        self.follows = defaultdict(set)

        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        
        self.follows[userId].add(userId)
        for i in self.follows[userId]:
            if i in self.posts:
                index = len(self.posts[i]) - 1
                time, tweetId = self.posts[i][index]
                minHeap.append((time, tweetId, i, index - 1))
        
        heapq.heapify(minHeap)

        while minHeap and len(res) < 10:
            time, tweetId, followeeId, index = heapq.heappop(minHeap) 
            res.append(tweetId)
            if index >= 0:
                time, tweetId = self.posts[followeeId][index]
                heapq.heappush(minHeap, (time, tweetId, followeeId, index - 1))

        self.follows[userId].discard(userId)
        return res
        



    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
        
        
