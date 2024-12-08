class Solution:
    def isPalindrome(self, s: str) -> bool:
        l: int = 0
        r: int = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1

        return True

    def isPalindrome2(self, s: str) -> bool:
        """time complexity: O(n)"""
        left: int = 0
        right: int = len(s) - 1
        while left <= right:
            while left <= right and not s[left].isalnum():
                left += 1
            while left <= right and not s[right].isalnum():
                right -= 1
            if left <= right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True


def test_isPalindrome_case_1():
    # arrange
    s: str = "A man, a plan, a canal: Panama"
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isPalindrome(s)

    # assert
    assert expected == actual


def test_isPalindrome_case_2():
    # arrange
    s: str = "race a car"
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isPalindrome(s)

    # assert
    assert expected == actual


def test_isPalindrome_case_3():
    # arrange
    s: str = " "
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isPalindrome(s)

    # assert
    assert expected == actual


def test_isPalindrome_case_4():
    # arrange
    s: str = ",."
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.isPalindrome(s)

    # assert
    assert expected == actual


def test_isPalindrome_case_5():
    # arrange
    s: str = "0P"
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.isPalindrome(s)

    # assert
    assert expected == actual
