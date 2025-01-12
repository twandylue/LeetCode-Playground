class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """time complexity: O(n)"""
        i: int = len(a) - 1
        j: int = len(b) - 1
        carry: int = 0
        result: str = ""
        while i >= 0 or j >= 0 or carry > 0:
            accu: int = carry
            if i >= 0:
                num: int = int(a[i])
                accu += num
                i -= 1
            if j >= 0:
                num: int = int(b[j])
                accu += num
                j -= 1
            digit: str = str(accu % 2)
            carry = accu // 2
            result += digit
        return result[::-1]


def test_addBinary_case_1():
    # arrange
    a: str = "11"
    b: str = "1"
    expected: str = "100"

    # act
    actual = Solution().addBinary(a, b)

    # assert
    assert expected == actual


def test_addBinary_case_2():
    # arrange
    a: str = "1010"
    b: str = "1011"
    expected: str = "10101"

    # act
    actual = Solution().addBinary(a, b)

    # assert
    assert expected == actual
