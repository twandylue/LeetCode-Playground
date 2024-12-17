import heapq

UserId = int
TweetId = int
Time = int


class Twitter:
    def __init__(self):
        self._time: int = 0
        self._follow_map: dict[UserId, set[UserId]] = {}
        self._tweet_map: dict[UserId, list[tuple[Time, TweetId]]] = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        """time complexity: O(1)"""
        if userId not in self._tweet_map:
            self._tweet_map[userId] = [(self._time, tweetId)]
        else:
            self._tweet_map[userId].append((self._time, tweetId))
        self._time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """time complexity: O(n) wherer n is the number of tweets"""
        min_heap: list[tuple[int, int]] = []
        result: list[int] = []
        if userId not in self._follow_map:
            self._follow_map[userId] = set([userId])
        else:
            self._follow_map[userId].add(userId)
        for followerId in self._follow_map[userId]:
            if followerId not in self._tweet_map:
                continue
            index: int = len(self._tweet_map[followerId]) - 1
            time, tweetId = self._tweet_map[followerId][index]
            heapq.heappush(min_heap, (time, tweetId, followerId, index - 1))
        while len(min_heap) > 0 and len(result) < 10:
            time, tweetId, followerId, index = heapq.heappop(min_heap)
            result.append(tweetId)
            if index >= 0:
                time, tweetId = self._tweet_map[followerId][index]
                heapq.heappush(min_heap, (time, tweetId, followerId, index - 1))
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """time complexity: O(1)"""
        if followerId not in self._follow_map:
            self._follow_map[followerId] = set([followeeId])
            return
        self._follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """time complexity: O(1)"""
        if followerId not in self._follow_map:
            return
        self._follow_map[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
def test_Twitter_case_1():
    tw = Twitter()
    tw.postTweet(1, 5)
    nt = tw.getNewsFeed(1)
    assert [5] == nt

    tw.follow(1, 2)
    tw.postTweet(2, 6)
    nt = tw.getNewsFeed(1)
    assert [6, 5] == nt

    tw.unfollow(1, 2)
    nt = tw.getNewsFeed(1)
    assert [5] == nt


def test_Twitter_case_2():
    tw = Twitter()
    tw.postTweet(1, 1)
    nt = tw.getNewsFeed(1)
    assert [1] == nt

    tw.follow(2, 1)
    nt = tw.getNewsFeed(2)
    assert [1] == nt

    tw.unfollow(2, 1)
    nt = tw.getNewsFeed(2)
    assert [] == nt


def test_Twitter_case_3():
    tw = Twitter()
    tw.postTweet(1, 4)
    tw.postTweet(2, 5)
    tw.unfollow(1, 2)

    nt = tw.getNewsFeed(1)
    assert [4] == nt
