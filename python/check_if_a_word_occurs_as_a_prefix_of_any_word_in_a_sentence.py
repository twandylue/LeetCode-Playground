class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words: list[str] = sentence.split(" ")
        for i in range(len(words)):
            if self.isPrefix(searchWord, words[i]):
                return i + 1
        return -1

    def isPrefix(self, searchWord: str, word: str) -> bool:
        if len(word) < len(searchWord):
            return False
        i: int = 0
        while i < len(searchWord):
            if searchWord[i] != word[i]:
                return False
            i += 1
        return True


def test_isPrefixOfWord_case_1():
    # arrange
    sentence: str = "i love eating burger"
    searchWord: str = "burg"
    expected: int = 4

    # act
    actual = Solution().isPrefixOfWord(sentence, searchWord)

    # assert
    assert expected == actual


def test_isPrefixOfWord_case_2():
    # arrange
    sentence: str = "i am tired"
    searchWord: str = "you"
    expected: int = -1

    # act
    actual = Solution().isPrefixOfWord(sentence, searchWord)

    # assert
    assert expected == actual
