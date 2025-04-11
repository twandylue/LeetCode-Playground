class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        """time complexity: O(n * 4^n)"""
        result: list[str] = []
        subset: list[str] = []
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
            self.dfs(0, digitToCharDict, subset, result, digits)
        return result

    def dfs(
        self,
        i: int,
        digitToCharDict: dict[str, str],
        subset: list[str],
        result: list[list[str]],
        digits: str,
    ) -> None:
        if i == len(digits):
            result.append("".join(subset))
            return
        for c in digitToCharDict[digits[i]]:
            subset.append(c)
            self.dfs(i + 1, digitToCharDict, subset, result, digits)
            subset.pop()


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
