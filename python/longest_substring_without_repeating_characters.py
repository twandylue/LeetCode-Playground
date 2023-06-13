class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet: set[str] = set()
        maxLength: int = 0
        l: int = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                if l < len(s):
                    l += 1
                else:
                    return 0

            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)

        return maxLength


def test_lengthOfLongestSubstring_case_1():
    # arrange
    s: str = "abcabcbb"
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.lengthOfLongestSubstring(s)

    # assert
    assert expected == actual


def test_lengthOfLongestSubstring_case_2():
    # arrange
    s: str = "bbbb"
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.lengthOfLongestSubstring(s)

    # assert
    assert expected == actual


def test_lengthOfLongestSubstring_case_3():
    # arrange
    s: str = "pwwkew"
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.lengthOfLongestSubstring(s)

    # assert
    assert expected == actual
