class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """time complexity: O(n * 4^n)"""
        result: list[str] = []
        curStr: str = ""
        digitToCharDict: dict[str, str] = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if len(digits) > 0:
            self.bfs(0, result, curStr, digits, digitToCharDict)

        return result

    def bfs(
        self,
        pos: int,
        result: list[str],
        curStr: str,
        digits: str,
        digitToCharDict: dict[str, str],
    ) -> None:
        if len(curStr) == len(digits):
            result.append(curStr)
            return
        for c in digitToCharDict[digits[pos]]:
            self.bfs(pos + 1, result, curStr + c, digits, digitToCharDict)


def test_letterCombinations_case_1():
    # arrange
    digits: str = "23"
    expected: list[str] = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

    # act
    solution = Solution()
    actual = solution.letterCombinations(digits)

    # assert
    assert actual == expected


def test_letterCombinations_case_2():
    # arrange
    digits: str = ""
    expected: list[str] = []

    # act
    solution = Solution()
    actual = solution.letterCombinations(digits)

    # assert
    assert actual == expected


def test_letterCombinations_case_3():
    # arrange
    digits: str = "2"
    expected: list[str] = ["a", "b", "c"]

    # act
    solution = Solution()
    actual = solution.letterCombinations(digits)

    # assert
    assert actual == expected
