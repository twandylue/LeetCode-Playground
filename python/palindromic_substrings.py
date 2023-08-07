class Solution:
    def countSubstrings(self, s: str) -> int:
        result: int = 0
        for i in range(len(s)):
            l: int = i
            r: int = i
            while r < len(s) and s[l] == s[r]:
                result += 1
                if l > 0:
                    l -= 1
                    r += 1
                else:
                    break
            l = i
            r = i + 1
            while r < len(s) and s[l] == s[r]:
                result += 1
                if l > 0:
                    l -= 1
                    r += 1
                else:
                    break

        return result


def test_countSubstrings_case_1():
    # arrange
    s: str = "abc"
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.countSubstrings(s)

    # assert
    assert expected == actual


def test_countSubstrings_case_2():
    # arrange
    s: str = "aaa"
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.countSubstrings(s)

    # assert
    assert expected == actual
