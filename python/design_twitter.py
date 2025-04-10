from collections import defaultdict
import heapq

UserId = int
TweetId = int
Time = int


class Twitter:
    def __init__(self):
        self._twitter_map: dict[UserId, list[tuple[Time, TweetId]]] = defaultdict(
            list
        )  # user id -> list of (time, tweet id)
        self._follow_map: dict[UserId, set[UserId]] = defaultdict(
            set
        )  # user1 id -> set of user2 id
        self._time: Time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """time complexity: O(1)"""
        self._twitter_map[userId].append((self._time, tweetId))
        self._time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        """time complexity: O(n) wherer n is the number of tweets"""
        min_heap: list[int] = []
        # User's tweets
        for u_t, u_tweet_id in self._twitter_map[userId]:
            heapq.heappush(min_heap, (u_t, u_tweet_id))

        # Followees' tweets
        followees: list[int] = list(self._follow_map[userId])
        for followee in followees:
            for f_t, f_tweet_id in self._twitter_map[followee]:
                heapq.heappush(min_heap, (f_t, f_tweet_id))

        # Get the result
        result: list[int] = []
        for _ in range(10):
            if len(min_heap) > 0:
                _, id = heapq.heappop(min_heap)
                result.append(id)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """time complexity: O(1)"""
        # Cannot follow yourself
        if followerId == followeeId:
            return
        self._follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """time complexity: O(1)"""
        if followeeId in self._follow_map[followerId]:
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
