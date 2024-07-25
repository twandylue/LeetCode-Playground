class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        """time complexity: O(n * m), where n is the number of words and m is the length of the longest word."""
        order_id: dict[str, int] = {c: i for i, c in enumerate(order)}
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if order_id[w1[j]] > order_id[w2[j]]:
                        return False
                    break
        return True


def test_isAlienSorted_case_1():
    # arrange
    words: list[str] = ["hello", "leetcode"]
    order: str = "hlabcdefgijkmnopqrstuvwxyz"
    expected: bool = True

    # act
    solution = Solution()
    actual: bool = solution.isAlienSorted(words, order)

    # assert
    assert expected == actual


def test_isAlienSorted_case_2():
    # arrange
    words: list[str] = ["word", "world", "row"]
    order: str = "worldabcefghijkmnpqstuvxyz"
    expected: bool = False

    # act
    solution = Solution()
    actual: bool = solution.isAlienSorted(words, order)

    # assert
    assert expected == actual


def test_isAlienSorted_case_3():
    # arrange
    words: list[str] = ["apple", "app"]
    order: str = "abcdefghijklmnopqrstuvwxyz"
    expected: bool = False

    # act
    solution = Solution()
    actual: bool = solution.isAlienSorted(words, order)

    # assert
    assert expected == actual
