class Solution:
    def countBits(self, n: int) -> list[int]:
        """time complexity: O(32 * n), space complexity: O(n)"""
        result: list[int] = []
        for i in range(n + 1):
            bits: int = self.count_bits(i)
            result.append(bits)
        return result

    def count_bits(self, i: int) -> int:
        result: int = 0
        for j in range(32):
            if i & (1 << j):
                result += 1
        return result

    def countBits_2(self, n: int) -> list[int]:
        """time complexity: O(n), space complexity: O(n)"""
        result: list[int] = [0] * (n + 1)
        for i in range(1, n + 1):
            result[i] = result[i // 2] + (1 if i % 2 > 0 else 0)
        return result


def test_countBits_case_1():
    # arrange
    n: int = 2
    expected: list[int] = [0, 1, 1]

    # act
    actual = Solution().countBits(n)

    # assert
    assert expected == actual


def test_countBits_case_2():
    # arrange
    n: int = 5
    expected: list[int] = [0, 1, 1, 2, 1, 2]

    # act
    actual = Solution().countBits(n)

    # assert
    assert expected == actual
