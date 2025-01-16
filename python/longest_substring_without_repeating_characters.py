class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """time complexity: O(n), space complexity: O(n)"""
        result: int = 0
        char_set: set[str] = set()
        l: int = 0
        for r in range(len(s)):
            while l < r and s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            result = max(result, r - l + 1)

        return result


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
