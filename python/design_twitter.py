import heapq
from typing import Set, Tuple

UserId = int
TweetId = int
Time = int


class Twitter:
    def __init__(self):
        self.time: int = 0
        self.userMap: dict[UserId, Set[UserId]] = dict()
        self.tweetsMap: dict[UserId, list[Tuple[Time, TweetId]]] = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.userMap:
            self.userMap[userId] = set()

        if userId in self.tweetsMap:
            self.tweetsMap[userId].append((-self.time, tweetId))
        else:
            self.tweetsMap[userId] = [(-self.time, tweetId)]

        self.time -= 1

        return None

    def getNewsFeed(self, userId: int) -> list[int]:
        recents: list[TweetId] = []
        maxHeap: list[Tuple[Time, TweetId]] = []
        heapq.heapify(maxHeap)

        if userId not in self.userMap:
            return recents

        if userId in self.tweetsMap:
            for t in self.tweetsMap[userId]:
                heapq.heappush(maxHeap, t)

        for u in self.userMap[userId]:
            if u in self.tweetsMap:
                for t in self.tweetsMap[u]:
                    heapq.heappush(maxHeap, t)

        return [n[1] for n in heapq.nlargest(10, maxHeap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userMap:
            self.userMap[followerId].add(followeeId)
        else:
            self.userMap[followerId] = {followeeId}

        return None

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.userMap:
            self.userMap[followerId].discard(followeeId)

        return None


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
