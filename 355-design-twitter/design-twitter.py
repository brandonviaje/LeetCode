class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1 #update timestamp

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = [] # max heap for the most recent

        # copy userIds
        users = self.follows[userId].copy()
        users.add(userId) 

        for userId in users:
            for time, tid in self.tweets[userId][-10:]: 
                heapq.heappush(heap, (-time, tid))

        result = []

        # while heap not empty or result not 10 tweets yet
        while heap and len(result) < 10:
            result.append(heapq.heappop(heap)[1]) # only add the tweet id

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        # follow if ids are different
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # unfollow if ids are different
        if followerId != followeeId:
            self.follows[followerId].discard(followeeId)
        
# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)