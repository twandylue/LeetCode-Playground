import heapq


class Solution:
    def maxScore(self, nums1: list[int], nums2: list[int], k: int) -> int:
        """time complexity: O(nlogn), space complexity: O(k)"""
        result: int = 0
        pairs: list[tuple[int, int]] = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
        n1_sum: int = 0
        min_heap: list[int] = []
        for n1, n2 in pairs:
            n1_sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) > k:
                n1_pop: int = heapq.heappop(min_heap)
                n1_sum -= n1_pop
            if len(min_heap) == k:
                result = max(result, n1_sum * n2)
        return result


def test_maxScore_case_1():
    """This is a test case for getOrder"""
    # arrange
    nums1: list[int] = [1, 3, 3, 2]
    nums2: list[int] = [2, 1, 3, 4]
    k: int = 3
    expected: int = 12

    # act
    solution = Solution()
    actual = solution.maxScore(nums1, nums2, k)

    # assert
    assert expected == actual


def test_maxScore_case_2():
    """This is a test case for getOrder"""
    # arrange
    nums1: list[int] = [4, 2, 3, 1, 1]
    nums2: list[int] = [7, 5, 10, 9, 6]
    k: int = 1
    expected: int = 30

    # act
    solution = Solution()
    actual = solution.maxScore(nums1, nums2, k)

    # assert
    assert expected == actual
