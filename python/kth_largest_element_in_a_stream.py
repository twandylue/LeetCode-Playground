import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self._min_heap: list[int] = nums
        self._k: int = k
        heapq.heapify(self._min_heap)
        while len(self._min_heap) > self._k:
            heapq.heappop(self._min_heap)

    def add(self, val: int) -> int:
        """time complexity: O(log(k))"""
        heapq.heappush(self._min_heap, val)
        if len(self._min_heap) > self._k:
            heapq.heappop(self._min_heap)
        return self._min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
def test_KthLargest_case_1():
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    assert 4 == kthLargest.add(3)
    assert 5 == kthLargest.add(5)
    assert 5 == kthLargest.add(10)
    assert 8 == kthLargest.add(9)
    assert 8 == kthLargest.add(4)
