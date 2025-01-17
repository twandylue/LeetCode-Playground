import random


class Solution:

    def __init__(self, w: list[int]):
        # Step 1: Create the prefix sum array
        self._prefix_sums: list[int] = [0] * len(w)
        prefix_sum: int = 0
        for i in range(len(w)):
            prefix_sum += w[i]
            self._prefix_sums[i] = prefix_sum
        self._total_sum = prefix_sum

    def pickIndex(self) -> int:
        # Step 2: Generate a random number in the range [1, total_sum]
        target: int = random.randint(1, self._total_sum)

        # Step 3: Use the lower bound search to find the target index
        l: int = 0
        r: int = len(self._prefix_sums) - 1
        while l < r:
            mid: int = (l + r) // 2
            if self._prefix_sums[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
