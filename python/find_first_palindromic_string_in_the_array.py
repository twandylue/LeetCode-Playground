class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.is_parli(word):
                return word
        return ""

    def is_parli(self, word: str) -> bool:
        i: int = 0
        j: int = len(word) - 1
        while i < j:
            if word[i] != word[j]:
                return False
            i += 1
            j -= 1
        return True


def test_firstPalindrome_case_1():
    # arrange
    words: list[str] = ["abc", "car", "ada", "racecar", "cool"]
    expected: str = "ada"

    # act
    solution = Solution()
    actual = solution.firstPalindrome(words)

    # assert
    assert expected == actual


def test_firstPalindrome_case_2():
    # arrange
    words: list[str] = ["notapalindrome", "racecar"]
    expected: str = "racecar"

    # act
    solution = Solution()
    actual = solution.firstPalindrome(words)

    # assert
    assert expected == actual


def test_firstPalindrome_case_3():
    # arrange
    words: list[str] = ["def", "ghi"]
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.firstPalindrome(words)

    # assert
    assert expected == actual
