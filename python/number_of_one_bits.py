class Solution:
    def hammingWeight(self, n: int) -> int:
        """time complexity: O(1)"""
        result: int = 0
        for i in range(32):
            if n & (1 << i) != 0:
                result += 1
        return result


def test_hammingWeight_case_1():
    # arrange
    n: int = 11
    expected: int = 3

    # act
    actual = Solution().countBits(n)

    # assert
    assert expected == actual


def test_hammingWeight_case_2():
    # arrange
    n: int = 128
    expected: int = 1

    # act
    actual = Solution().countBits(n)

    # assert
    assert expected == actual


def test_hammingWeight_case_3():
    # arrange
    n: int = 2147483645
    expected: int = 30

    # act
    actual = Solution().countBits(n)

    # assert
    assert expected == actual
