import heapq


class Solution:
    def isNStraightHand(self, hand: list[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count: dict[int, int] = dict()
        for i in hand:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        minHeap: list[int] = list(count.keys())
        heapq.heapify(minHeap)

        while len(minHeap) > 0:
            first: int = minHeap[0]
            for n in range(first, first + groupSize):
                if n not in count:
                    return False
                count[n] -= 1
                if count[n] == 0:
                    if n != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)

        return True


def test_isNStraightHand_case_1():
    # arrange
    hand: list[int] = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize: int = 3
    expected: bool = True

    # act
    actual = Solution().isNStraightHand(hand, groupSize)

    # assert
    assert actual == expected


def test_isNStraightHand_case_2():
    # arrange
    hand: list[int] = [1, 2, 3, 4, 5]
    groupSize: int = 4
    expected: bool = False

    # act
    actual = Solution().isNStraightHand(hand, groupSize)

    # assert
    assert actual == expected
