class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """time complexity: O(n)"""
        left: int = 0
        curr_cost: int = 0
        result: int = 0
        for right in range(len(t)):
            curr_cost += abs(ord(s[right]) - ord(t[right]))
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            result = max(result, right - left + 1)
        return result


def test_equalSubstring_case_1():
    # arrange
    s: str = "abcd"
    t: str = "bcdf"
    maxCost: int = 3
    expected: int = 3

    # act
    actual = Solution().equalSubstring(s, t, maxCost)

    # assert
    assert expected == actual


def test_equalSubstring_case_2():
    # arrange
    s: str = "abcd"
    t: str = "cdef"
    maxCost: int = 3
    expected: int = 1

    # act
    actual = Solution().equalSubstring(s, t, maxCost)

    # assert
    assert expected == actual


def test_equalSubstring_case_3():
    # arrange
    s: str = "abcd"
    t: str = "acde"
    maxCost: int = 0
    expected: int = 1

    # act
    actual = Solution().equalSubstring(s, t, maxCost)

    # assert
    assert expected == actual
