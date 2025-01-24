import heapq


class Solution:
    def reorderLogFiles(self, logs: list[str]) -> list[str]:
        """time complexity: O(nlogn), space complexity: O(n)"""
        digits: list[str] = []
        letters: list[str] = []
        min_heap: list[tuple[str, str]] = []
        for log in logs:
            data: str = log.split(" ", 1)[1]
            if data[0].isdigit():
                digits.append(log)
            else:
                heapq.heappush(min_heap, (data, log))
        while len(min_heap) > 0:
            letters.append(heapq.heappop(min_heap)[1])
        return letters + digits


def test_reorderLogFiles_case_1():
    # arrange
    logs: list[str] = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    expected: list[str] = [
        "let1 art can",
        "let3 art zero",
        "let2 own kit dig",
        "dig1 8 1 5 1",
        "dig2 3 6",
    ]

    # act
    actual = Solution().reorderLogFiles(logs)

    # assert
    assert expected == actual


def test_reorderLogFiles_case_2():
    # arrange
    logs: list[str] = [
        "a1 9 2 3 1",
        "g1 act car",
        "zo4 4 7",
        "ab1 off key dog",
        "a8 act zoo",
    ]
    expected: list[str] = [
        "g1 act car",
        "a8 act zoo",
        "ab1 off key dog",
        "a1 9 2 3 1",
        "zo4 4 7",
    ]

    # act
    actual = Solution().reorderLogFiles(logs)

    # assert
    assert expected == actual


def test_reorderLogFiles_case_1():
    # arrange
    logs: list[str] = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    expected: list[str] = [
        "let1 art can",
        "let3 art zero",
        "let2 own kit dig",
        "dig1 8 1 5 1",
        "dig2 3 6",
    ]

    # act
    actual = Solution().reorderLogFiles(logs)

    # assert
    assert expected == actual


def test_reorderLogFiles_case_2():
    # arrange
    logs: list[str] = [
        "a1 9 2 3 1",
        "g1 act car",
        "zo4 4 7",
        "ab1 off key dog",
        "a8 act zoo",
    ]
    expected: list[str] = [
        "g1 act car",
        "a8 act zoo",
        "ab1 off key dog",
        "a1 9 2 3 1",
        "zo4 4 7",
    ]

    # act
    actual = Solution().reorderLogFiles(logs)

    # assert
    assert expected == actual
