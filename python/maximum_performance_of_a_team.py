import heapq


class Solution:
    def maxPerformance(
        self, n: int, speed: list[int], efficiency: list[int], k: int
    ) -> int:
        """
        NOTE:
        time complexity: O(nlogn), space complexity: O(n), where n is the length of speed and efficiency
        Besides, this one is pretty similar to LC. 2542. Maximum Subsequence Score
        """
        result: int = 0
        s: int = 0
        engineers: list[tuple[int, int]] = list(zip(efficiency, speed))
        ## NOTE: This is another way to create engineers
        # engineers: list[tuple[int, int]] = [(e, s) for e, s in zip(efficiency, speed)]
        engineers.sort(reverse=True)
        min_heap: list[int] = []
        for eff, spd in engineers:
            if len(min_heap) == k:
                s -= heapq.heappop(min_heap)
            s += spd
            heapq.heappush(min_heap, spd)
            result = max(result, eff * s)
        return result % (10**9 + 7)


def test_maxPerformance_case_1():
    """This is a test case for maxPerformance"""
    # arrange
    n: int = 6
    speed: list[int] = [2, 10, 3, 1, 5, 8]
    efficiency: list[int] = [5, 4, 3, 9, 7, 2]
    k: int = 2
    expected: int = 60

    # act
    solution = Solution()
    actual = solution.maxPerformance(n, speed, efficiency, k)

    # assert
    assert expected == actual


def test_maxPerformance_case_2():
    """This is a test case for maxPerformance"""
    # arrange
    n: int = 6
    speed: list[int] = [2, 10, 3, 1, 5, 8]
    efficiency: list[int] = [5, 4, 3, 9, 7, 2]
    k: int = 3
    expected: int = 68

    # act
    solution = Solution()
    actual = solution.maxPerformance(n, speed, efficiency, k)

    # assert
    assert expected == actual
