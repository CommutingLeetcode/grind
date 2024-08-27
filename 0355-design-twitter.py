class Twitter:

    def __init__(self):
        self.userToFollowee = defaultdict(set)
        self.userToTweets = defaultdict(list)
        self.count = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # append self.count and tweetId to user map
        self.count -= 1
        self.userToTweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        output = []
        # get every list of tweets from (userId and all ids it follows)
        ids = set()
        for currId in self.userToFollowee[userId]:
            ids.add(currId)
        ids.add(userId)

        # append from k groups
        for currId in ids:
            if len(self.userToTweets[currId]) > 0:
                heapq.heappush(minHeap, (self.userToTweets[currId][-1][0], self.userToTweets[currId][-1][1], len(self.userToTweets[currId]) - 1, currId))
        
        while minHeap and len(output) < 10:
            count, tweetId, i, currId = heapq.heappop(minHeap)
            output.append(tweetId)
            if i > 0:
                heapq.heappush(minHeap, (self.userToTweets[currId][i - 1][0], self.userToTweets[currId][i - 1][1], i - 1, currId))
        
        return output

    def follow(self, followerId: int, followeeId: int) -> None:
        # add followeeId to followerId set
        self.userToFollowee[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userToFollowee:
            self.userToFollowee[followerId].remove(followeeId)



# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

'''

'''
