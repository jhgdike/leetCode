import collections


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 0
        self.user_map = collections.defaultdict(set)
        self.user_post = collections.defaultdict(list)

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.cnt += 1
        self.user_post[userId].append((tweetId, self.cnt))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        stack = []
        uid_post_index = {uid: len(self.user_post[uid]) - 1 for uid in self.user_map[userId] | {userId}}
        while len(stack) < 10:
            cur = None
            for uid, index in uid_post_index.items():
                if index >= 0 and (not cur or self.user_post[cur[0]][cur[1]][1] < self.user_post[uid][index][1]):
                    cur = (uid, index)
            if not cur:
                break
            stack.append(self.user_post[cur[0]][cur[1]][0])
            uid_post_index[cur[0]] -= 1
        return stack

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.user_map[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.user_map[followerId]:
            self.user_map[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

input0 = ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
input1 = [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
for i in range(1, len(input0)):
    print(getattr(obj, input0[i])(*input1[i]))

input0 = ["Twitter", "postTweet", "unfollow", "getNewsFeed"]
input1 = [[], [1, 5], [1, 1], [1]]
obj = Twitter()
for i in range(1, len(input0)):
    print(getattr(obj, input0[i])(*input1[i]))


input0 = ["Twitter","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","postTweet","getNewsFeed","follow","getNewsFeed"]
input1 = [[],[2,5],[1,3],[1,101],[2,13],[2,10],[1,2],[2,94],[2,505],[1,333],[1,22],[2],[2,1],[2]]
obj = Twitter()
for i in range(1, len(input0)):
    print(getattr(obj, input0[i])(*input1[i]))