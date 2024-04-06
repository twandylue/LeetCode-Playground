class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: list[str] = []
        for i in range(len(s)):
            if len(stack) > 0 and stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
        return "".join(stack)


def test_removeDuplicates_case_1():
    # arrange
    s: str = "abbaca"
    expected: str = "ca"

    # act
    solution = Solution()
    actual = solution.removeDuplicates(s)

    # assert
    assert expected == actual


def test_removeDuplicates_case_2():
    # arrange
    s: str = "azxxzy"
    expected: str = "ay"

    # act
    solution = Solution()
    actual = solution.removeDuplicates(s)

    # assert
    assert expected == actual
