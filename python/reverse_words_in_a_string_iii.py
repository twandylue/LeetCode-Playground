class Solution:
    def reverseWords(self, s: str) -> str:
        """time complexity: O(n)"""
        s: list[str] = list(s)
        left: int = 0
        for right in range(len(s)):
            if s[right] == " " or right == len(s) - 1:
                tmp_l, tmp_r = left, right - 1
                if right == len(s) - 1:
                    tmp_r = right
                while tmp_l < tmp_r:
                    tmp: str = s[tmp_l]
                    s[tmp_l] = s[tmp_r]
                    s[tmp_r] = tmp
                    tmp_l += 1
                    tmp_r -= 1
                left = right + 1
        return "".join(s)


def test_reverseWords_case_1():
    # arrange
    s: str = "Let's take LeetCode contest"
    expected: str = "s'teL ekat edoCteeL tsetnoc"

    # act
    solution = Solution()
    actual = solution.reverseWords(s)

    # assert
    assert expected == actual


def test_reverseWords_case_2():
    # arrange
    s: str = "Mr Ding"
    expected: str = "rM gniD"

    # act
    solution = Solution()
    actual = solution.reverseWords(s)

    # assert
    assert expected == actual
