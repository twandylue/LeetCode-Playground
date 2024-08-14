class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        """time complexity: O(n)"""
        w1: int = 0
        w2: int = 0
        i: int = 0
        j: int = 0
        while w1 < len(word1) and w2 < len(word2):
            if word1[w1][i] != word2[w2][j]:
                return False
            i += 1
            j += 1
            if i == len(word1[w1]):
                i = 0
                w1 += 1
            if j == len(word2[w2]):
                j = 0
                w2 += 1
        if w1 != len(word1) or w2 != len(word2):
            return False
        return True


def test_arrayStringsAreEqual_case_1():
    # arrange
    word1: list[str] = ["ab", "c"]
    word2: list[str] = ["a", "bc"]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.arrayStringsAreEqual(word1, word2)

    # assert
    assert expected == actual


def test_arrayStringsAreEqual_case_2():
    # arrange
    word1: list[str] = ["a", "cb"]
    word2: list[str] = ["ab", "c"]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.arrayStringsAreEqual(word1, word2)

    # assert
    assert expected == actual


def test_arrayStringsAreEqual_case_3():
    # arrange
    word1: list[str] = ["abc", "d", "defg"]
    word2: list[str] = ["abcddefg"]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.arrayStringsAreEqual(word1, word2)

    # assert
    assert expected == actual
