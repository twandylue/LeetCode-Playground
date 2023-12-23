class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1: int = 0
        w2: int = 0
        result: str = ""
        while w1 < len(word1) and w2 < len(word2):
            result += word1[w1]
            result += word2[w2]
            w1 += 1
            w2 += 1

        while w1 < len(word1):
            result += word1[w1]
            w1 += 1

        while w2 < len(word2):
            result += word2[w2]
            w2 += 1

        return result


def test_mergealternately_case_1():
    # arrange
    word1: str = "abc"
    word2: str = "pqr"
    expected: str = "apbqcr"

    # act
    solution = Solution()
    actual = solution.mergeAlternately(word1, word2)

    # assert
    assert expected == actual


def test_mergealternately_case_2():
    # arrange
    word1: str = "ab"
    word2: str = "pqrs"
    expected: str = "apbqrs"

    # act
    solution = Solution()
    actual = solution.mergeAlternately(word1, word2)

    # assert
    assert expected == actual


def test_mergealternately_case_3():
    # arrange
    word1: str = "abcd"
    word2: str = "pq"
    expected: str = "apbqcd"

    # act
    solution = Solution()
    actual = solution.mergeAlternately(word1, word2)

    # assert
    assert expected == actual
