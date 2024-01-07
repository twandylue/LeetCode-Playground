class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result: int = 0
        strArr: list[str] = [0] * 26
        currLen: int = 0
        l: int = 0
        r: int = 0
        while l < len(s) and r < len(s):
            strArr[ord(s[r]) - ord("A")] += 1
            currLen = r - l + 1
            if currLen - max(strArr) <= k:
                result = max(result, currLen)
            else:
                while currLen - max(strArr) > k:
                    strArr[ord(s[l]) - ord("A")] -= 1
                    l += 1
                    currLen -= 1
            r += 1

        return result


def test_characterReplacement_case_1():
    # arrange
    s: str = "ABAB"
    k: str = 2
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual


def test_characterReplacement_case_2():
    # arrange
    s: str = "AABABBA"
    k: str = 1
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual


def test_characterReplacement_case_3():
    # arrange
    s: str = "BAAA"
    k: str = 0
    expected: int = 3

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual


def test_characterReplacement_case_4():
    # arrange
    s: str = "ABBB"
    k: str = 2
    expected: int = 4

    # act
    solution = Solution()
    actual = solution.characterReplacement(s, k)

    # assert
    assert expected == actual
