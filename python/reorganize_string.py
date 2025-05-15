import heapq
from collections import defaultdict
from typing import Optional


class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        NOTE: time complexity O(nlogk), space complexity O(k), where n is the length of the string and k is the number of unique charactres
        1. Most frequent character should be placed first
        2. Use prev to store the previous character and skip it in the next iteration
        """
        result: str = ""
        counter: dict[str, int] = defaultdict(int)
        for c in s:
            counter[c] += 1
        max_heap: list[tuple[int, str]] = []
        for k, v in counter.items():
            heapq.heappush(max_heap, (-1 * v, k))
        prev: Optional[tuple[int, str]] = None
        while len(max_heap) > 0 or prev is not None:
            if len(max_heap) == 0 and prev is not None:
                return ""
            count, c = heapq.heappop(max_heap)
            result += c
            count += 1
            if prev is not None:
                heapq.heappush(max_heap, prev)
                prev = None
            if count < 0 and prev is None:
                prev = (count, c)
        return result


def test_reorganizeString_case_1():
    # arrange
    s: str = "aab"
    expected: str = "aba"

    # act
    solution = Solution()
    actual = solution.reorganizeString(s)

    # assert
    assert expected == actual


def test_reorganizeString_case_2():
    # arrange
    s: str = "aaab"
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.reorganizeString(s)

    # assert
    assert expected == actual
