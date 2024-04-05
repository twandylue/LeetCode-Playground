class Solution:
    def removeStars(self, s: str) -> str:
        """time complexity: O(n), space complexity: O(n)"""
        stack: list[str] = []
        for c in s:
            if len(stack) >= 0 and c == "*":
                stack.pop()
            else:
                stack.append(c)
        return "".join(stack)


def test_removeStars_case_1():
    # arrange
    s: str = "leet**cod*e"
    expected: str = "lecoe"

    # act
    solution = Solution()
    actual = solution.removeStars(s)

    # assert
    assert expected == actual


def test_removeStars_case_2():
    # arrange
    s: str = "erase*****"
    expected: str = ""

    # act
    solution = Solution()
    actual = solution.removeStars(s)

    # assert
    assert expected == actual
