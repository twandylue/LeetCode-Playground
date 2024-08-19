class Solution:
    def minimumLength(self, s: str) -> int:
        """time complexity: O(n)"""
        l: int = 0
        r: int = len(s) - 1
        while l < r and s[l] == s[r]:
            tmp: str = s[l]
            while l <= r and s[l] == tmp:
                l += 1
            while l <= r and s[r] == tmp:
                r -= 1
        return r - l + 1


def test_minimumLength_case_1():
    # arrange
    s: str = "ca"
    expected: int = 2

    # act
    solution = Solution()
    actual: int = solution.minimumLength(s)

    # assert
    assert expected == actual


def test_minimumLength_case_2():
    # arrange
    s: str = "cabaabac"
    expected: int = 0

    # act
    solution = Solution()
    actual: int = solution.minimumLength(s)

    # assert
    assert expected == actual


def test_minimumLength_case_3():
    # arrange
    s: str = "aabccabba"
    expected: int = 3

    # act
    solution = Solution()
    actual: int = solution.minimumLength(s)

    # assert
    assert expected == actual
