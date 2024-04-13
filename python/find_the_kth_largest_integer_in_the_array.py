import heapq


class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        """time complexity: O(nlogn), space complexity: O(n)"""
        min_heap: list[int] = [int(s) for s in nums]
        heapq.heapify(min_heap)
        while len(min_heap) > k:
            heapq.heappop(min_heap)
        return str(min_heap[0])

        ## NOTE: Another way
        # return str(heapq.nlargest(k, min_heap)[-1])


def test_kthLargestNumber_case_1():
    # arrange
    nums: list[str] = ["3", "6", "7", "10"]
    k: int = 4
    expected: int = "3"

    # act
    solution = Solution()
    actual = solution.kthLargestNumber(nums, k)

    # assert
    assert expected == actual


def test_kthLargestNumber_case_2():
    # arrange
    nums: list[str] = ["2", "21", "12", "1"]
    k: int = 3
    expected: int = "2"

    # act
    solution = Solution()
    actual = solution.kthLargestNumber(nums, k)

    # assert
    assert expected == actual


def test_kthLargestNumber_case_3():
    # arrange
    nums: list[str] = ["0", "0"]
    k: int = 2
    expected: int = "0"

    # act
    solution = Solution()
    actual = solution.kthLargestNumber(nums, k)

    # assert
    assert expected == actual
