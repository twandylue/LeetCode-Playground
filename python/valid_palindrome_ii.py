class Solution:
    def validPalindrome(self, s: str) -> bool:
        """time complexity: O(n), space complexity: O(1)"""
        if len(s) < 1:
            return True
        l: int = 0
        r: int = len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue

            return self.isPalindrome(s[l + 1 : r + 1]) or self.isPalindrome(s[l:r])

        return True

    def isPalindrome(self, s: str) -> bool:
        if len(s) < 1:
            return True
        l: int = 0
        r: int = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True


def test_validPalindrome_case_1():
    # arrange
    s: str = "aba"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.validPalindrome(s)

    # assert
    assert expected == actual


def test_validPalindrome_case_2():
    # arrange
    s: str = "abca"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.validPalindrome(s)

    # assert
    assert expected == actual


def test_validPalindrome_case_3():
    # arrange
    s: str = "abc"
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.validPalindrome(s)

    # assert
    assert expected == actual


def test_validPalindrome_case_4():
    # arrange
    s: str = "deeee"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.validPalindrome(s)

    # assert
    assert expected == actual
