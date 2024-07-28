import heapq


class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        """time complexity: O(nlogn), space complexity: O(n)"""
        max_heap: list[int] = []
        for i in range(len(heights) - 1):
            diff: int = heights[i + 1] - heights[i]
            if diff < 0:
                continue
            bricks -= diff
            heapq.heappush(max_heap, -1 * diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -1 * heapq.heappop(max_heap)
        return len(heights) - 1


def test_furthestBuilding_case_1():
    # arrange
    heights: list[int] = [4, 2, 7, 6, 9, 14, 12]
    bricks: int = 5
    ladders: int = 1
    expected: int = 4

    # act
    actual = Solution().furthestBuilding(heights, bricks, ladders)

    # assert
    assert actual == expected


def test_furthestBuilding_case_2():
    # arrange
    heights: list[int] = [4, 12, 2, 7, 3, 18, 20, 3, 19]
    bricks: int = 10
    ladders: int = 2
    expected: int = 7

    # act
    actual = Solution().furthestBuilding(heights, bricks, ladders)

    # assert
    assert actual == expected


def test_furthestBuilding_case_3():
    # arrange
    heights: list[int] = [14, 3, 19, 3]
    bricks: int = 17
    ladders: int = 0
    expected: int = 3

    # act
    actual = Solution().furthestBuilding(heights, bricks, ladders)

    # assert
    assert actual == expected
