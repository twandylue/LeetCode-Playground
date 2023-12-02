class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # NOTE: O(mn)
        index: int = 0
        curr: int = 0
        for i in range(len(haystack)):
            if i + len(needle) - 1 >= len(haystack):
                return -1
            else:
                s: int = i
                flag: bool = False
                for c in range(len(needle)):
                    if haystack[i] == needle[c]:
                        i += 1
                        flag = True
                        continue
                    flag = False
                    break
                if flag:
                    return s

        return -1


def test_strStr_case_1():
    # arrange
    haystack: str = "sadbutsad"
    needle: str = "sad"
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.strStr(haystack, needle)

    # assert
    assert expected == actual


def test_strStr_case_2():
    # arrange
    haystack: str = "leetcode"
    needle: str = "leeto"
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.strStr(haystack, needle)

    # assert
    assert expected == actual


def test_strStr_case_3():
    # arrange
    haystack: str = "mississippi"
    needle: str = "issip"
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.strStr(haystack, needle)

    # assert
    assert expected == actual
