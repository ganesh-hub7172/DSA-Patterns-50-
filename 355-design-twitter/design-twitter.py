import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId):
        heap = []

        users = self.follows[userId].copy()
        users.add(userId)

        for u in users:
            if self.tweets[u]:
                time, tweet = self.tweets[u][-1]
                index = len(self.tweets[u]) - 1
                heapq.heappush(heap, (time, tweet, u, index))

        result = []

        while heap and len(result) < 10:
            time, tweet, user, index = heapq.heappop(heap)
            result.append(tweet)

            if index > 0:
                next_time, next_tweet = self.tweets[user][index - 1]
                heapq.heappush(heap, (next_time, next_tweet, user, index - 1))

        return result

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.follows[followerId].discard(followeeId)
