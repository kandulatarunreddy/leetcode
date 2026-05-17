import heapq
from collections import defaultdict


class Twitter:

    def __init__(self):

        # -----------------------------------------
        # follow_map[user]
        #
        # Stores who a user follows
        #
        # Example:
        #
        # 1 -> {2,3}
        #
        # means user 1 follows 2 and 3
        # -----------------------------------------
        self.follow_map = defaultdict(set)

        # -----------------------------------------
        # tweet_map[user]
        #
        # Stores tweets:
        #
        # (timestamp, tweetId)
        #
        # Example:
        #
        # 1 -> [
        #   (-1,101),
        #   (-2,102)
        # ]
        # -----------------------------------------
        self.tweet_map = defaultdict(list)

        # Global timestamp
        #
        # Smaller value = newer tweet
        self.time = 0

    def postTweet(self, userId, tweetId):

        # -----------------------------------------
        # Add tweet
        #
        # Example:
        #
        # user 1 posts 101
        #
        # tweet_map[1]
        # [ (0,101) ]
        # -----------------------------------------
        self.tweet_map[userId].append((self.time, tweetId))

        # Decrease time
        #
        # Example:
        #
        # 0, -1, -2...
        #
        # newer tweet becomes smaller
        self.time -= 1

    def getNewsFeed(self, userId):

        result = []

        max_heap = []

        # -----------------------------------------
        # User always follows themselves
        # -----------------------------------------
        self.follow_map[userId].add(userId)

        # Get all followees
        followees = self.follow_map[userId]

        # -----------------------------------------
        # Add latest tweet from each user
        #
        # Example:
        #
        # heap:
        #
        # [
        #   (-5,101,user,idx),
        #   (-3,202,user,idx)
        # ]
        # -----------------------------------------
        for user in followees:

            if user in self.tweet_map:
                tweets = self.tweet_map[user]
                last_index = len(tweets) - 1
                timestamp, tweet_id = tweets[last_index]
                heapq.heappush(max_heap,(timestamp,tweet_id,user,last_index - 1))

        # -----------------------------------------
        # Get 10 most recent tweets
        # -----------------------------------------
        while max_heap and len(result) < 10:

            (timestamp,tweet_id,user,next_index) = heapq.heappop(max_heap)
            result.append(tweet_id)
            # -----------------------------------------
            # Push older tweet from same user
            #
            # Example:
            #
            # user had:
            # [101,102,103]
            #
            # after taking 103,
            # push 102
            # -----------------------------------------
            if next_index >= 0:
                next_timestamp, next_tweet = (self.tweet_map[user][next_index])
                heapq.heappush(max_heap,(next_timestamp,next_tweet,user,next_index - 1))

        return result

    def follow(self,followerId,followeeId):
        self.follow_map[followerId].add(followeeId)

    def unfollow(self,followerId,followeeId):

        # Cannot unfollow yourself
        if followerId != followeeId:
            self.follow_map[followerId].discard(followeeId)


# Example run in IntelliJ IDEA / PyCharm

twitter = Twitter()

twitter.postTweet(1, 5)

print(twitter.getNewsFeed(1))
# [5]

twitter.follow(1, 2)

twitter.postTweet(2, 6)

print(twitter.getNewsFeed(1))
# [6,5]

twitter.unfollow(1, 2)

print(twitter.getNewsFeed(1))
# [5]

# Time Complexity:
#
# postTweet()   -> O(1)
# follow()      -> O(1)
# unfollow()    -> O(1)
#
# getNewsFeed() -> O(F log F)
#
# F = number of followed users
#
# Space Complexity: O(T + F)
#
# T = total tweets
# F = follow relationships