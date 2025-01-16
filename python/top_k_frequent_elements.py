from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """time complexity: O(n) where n is the length of nums"""
        result: list[int] = []
        occur_map: dict[int, int] = {}
        bucket: list[list[int]] = []
        for i in range(len(nums) + 1):
            bucket.append([])
        for num in nums:
            if num not in occur_map:
                occur_map[num] = 1
            else:
                occur_map[num] += 1
        for key, val in occur_map.items():
            bucket[val].append(key)
        i: int = 0
        while k > 0 and i < len(nums):
            idx: int = len(nums) - i
            if len(bucket[idx]) > 0:
                result += bucket[idx]
                k -= len(bucket[idx])
            i += 1
        return result

    def topKFrequent2(self, nums: list[int], k: int) -> list[int]:
        """time complexity: O(nlogk) where n is the length of nums, k is the number of unique elements"""
        result: list[int] = []
        count_map: dict[int, int] = defaultdict(int)
        for num in nums:
            count_map[num] += 1
        min_heap: list[tuple[int, int]] = []
        for key, val in count_map.items():
            heapq.heappush(min_heap, (val, key))
        for _ in range(len(min_heap) - k):
            heapq.heappop(min_heap)
        while len(min_heap) > 0:
            count, num = heapq.heappop(min_heap)
            result.append(num)
        return result


def test_topKFrequent_case_1():
    # Arrange
    nums: list[int] = [1, 1, 1, 2, 2, 3]
    k: int = 2
    expected: list[int] = [1, 2]

    # Act
    actual: list[int] = Solution().topKFrequent(nums, k)

    # Assert
    assert expected == actual


def test_topKFrequent_case_2():
    # Arrange
    nums: list[int] = [1]
    k: int = 1
    expected: list[int] = [1]

    # Act
    actual: list[int] = Solution().topKFrequent(nums, k)

    # Assert
    assert expected == actual


def test_topKFrequent_case_3():
    # Arrange
    nums: list[int] = [4, 1, -1, 2, -1, 2, 3]
    k: int = 2
    expected: list[int] = [-1, 2]

    # Act
    actual: list[int] = Solution().topKFrequent(nums, k)

    # Assert
    assert expected == actual
