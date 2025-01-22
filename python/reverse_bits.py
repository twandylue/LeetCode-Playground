class Solution:
    def reverseBits(self, n: int) -> int:
        """time complexity: O(1)"""
        result: int = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n = n >> 1
        return result


def test_reverseBits_case_1():
    # arrange
    n: int = 0b00000010100101000001111010011100
    expected: int = 0b00111001011110000010100101000000

    # act
    actual = Solution().reverseBits(n)

    # assert
    assert expected == actual


def test_reverseBits_case_2():
    # arrange
    n: int = 0b11111111111111111111111111111101
    expected: int = 0b10111111111111111111111111111111

    # act
    actual = Solution().reverseBits(n)

    # assert
    assert expected == actual
