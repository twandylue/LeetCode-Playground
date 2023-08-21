from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordlist: list[str]) -> int:
        if endWord not in wordlist:
            return 0

        wordlist.append(beginWord)
        neiborWords: dict[str, list[str]] = dict()
        visited: set[str] = set([beginWord])
        queue: deque[str] = deque([beginWord])
        result: int = 1

        for word in wordlist:
            for i in range(0, len(word)):
                pattern: str = word[:i] + "*" + word[i + 1 :]
                if pattern in neiborWords:
                    neiborWords[pattern].append(word)
                else:
                    neiborWords[pattern] = [word]

        while len(queue) > 0:
            for _ in range(0, len(queue)):
                word: str = queue.popleft()
                if word == endWord:
                    return result
                for i in range(0, len(word)):
                    pattern: str = word[:i] + "*" + word[i + 1 :]
                    for nextWord in neiborWords[pattern]:
                        if nextWord not in visited:
                            queue.append(nextWord)
                            visited.add(nextWord)

            result += 1

        return 0


def test_ladderLength_case_1():
    # Arrange
    beginWord: str = "hit"
    endWord: str = "cog"
    wordlist: list[str] = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected: int = 5

    # Act
    result: int = Solution().ladderLength(beginWord, endWord, wordlist)

    # Assert
    assert result == expected


def test_ladderLength_case_2():
    # Arrange
    beginWord: str = "hit"
    endWord: str = "cog"
    wordlist: list[str] = ["hot", "dot", "dog", "lot", "log"]
    expected: int = 0

    # Act
    result: int = Solution().ladderLength(beginWord, endWord, wordlist)

    # Assert
    assert result == expected


def test_ladderLength_case_3():
    # Arrange
    beginWord: str = "hot"
    endWord: str = "dog"
    wordlist: list[str] = ["hot", "dog"]
    expected: int = 0

    # Act
    result: int = Solution().ladderLength(beginWord, endWord, wordlist)

    # Assert
    assert result == expected
