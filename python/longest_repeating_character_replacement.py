class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result: int = 0
        charCount: list[int] = [0] * 26
        l: int = 0
        for r in range(len(s)):
            charCount[ord(s[r]) - ord("A")] += 1
            currLen: int = r - l + 1
            if currLen - max(charCount) <= k:
                result = max(result, currLen)
            else:
                while currLen - max(charCount) > k:
                    charCount[ord(s[l]) - ord("A")] -= 1
                    l += 1
                    currLen -= 1

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
