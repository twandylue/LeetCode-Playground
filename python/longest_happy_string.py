import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        NOTE:
        Time complexity: O(n), space complexity: O(n), where n is the sum of a, b, and c.
        Since the size of the heap is at most 3, the time complexity is O(1) for each operation.
        So, the time complexity is O(n) in total, where n is the sum of a, b, and c.
        """
        max_heap: list[tuple[int, str]] = []
        for count, char in [(a, "a"), (b, "b"), (c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (-count, char))
        result: str = ""
        while len(max_heap) > 0:
            cnt, c = heapq.heappop(max_heap)
            if len(result) > 1 and c == result[-1] and c == result[-2]:
                if len(max_heap) == 0:
                    break
                cnt_2, c_2 = heapq.heappop(max_heap)
                result += c_2
                cnt_2 += 1
                if cnt_2 < 0:
                    heapq.heappush(max_heap, (cnt_2, c_2))
            else:
                result += c
                cnt += 1
            if cnt < 0:
                heapq.heappush(max_heap, (cnt, c))
        return result


def test_longestDiverseString_case_1():
    # arrange
    a: int = 1
    b: int = 1
    c: int = 7
    expected: str = "ccaccbcc"

    # act
    solution = Solution()
    actual = solution.longestDiverseString(a, b, c)

    # assert
    assert expected == actual


def test_longestDiverseString_case_2():
    # arrange
    a: int = 7
    b: int = 1
    c: int = 0
    expected: str = "aabaa"

    # act
    solution = Solution()
    actual = solution.longestDiverseString(a, b, c)

    # assert
    assert expected == actual
