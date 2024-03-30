class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l: int = 0
        r: int = len(s) - 1
        while l < r:
            tmp: str = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1


def test_reverseString_case_1():
    # arrange
    s: list[str] = ["h", "e", "l", "l", "o"]
    expected: list[str] = ["o", "l", "l", "e", "h"]

    # act
    solution = Solution()
    solution.reverseString(s)

    # assert
    assert expected == s
