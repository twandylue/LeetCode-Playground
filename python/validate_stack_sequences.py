class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        stack: list[int] = list()
        p: int = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while p < len(popped) and len(stack) > 0 and popped[p] == stack[-1]:
                stack.pop()
                p += 1
        return len(stack) == 0


def test_validateStackSequences_case_1():
    # arrange
    pushed: list[int] = [1, 2, 3, 4, 5]
    popped: list[int] = [4, 5, 3, 2, 1]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.validateStackSequences(pushed, popped)

    # assert
    assert expected == actual


def test_validateStackSequences_case_2():
    # arrange
    pushed: list[int] = [1, 2, 3, 4, 5]
    popped: list[int] = [4, 3, 5, 1, 2]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.validateStackSequences(pushed, popped)

    # assert
    assert expected == actual


def test_validateStackSequences_case_3():
    # arrange
    pushed: list[int] = [1, 0]
    popped: list[int] = [1, 0]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.validateStackSequences(pushed, popped)

    # assert
    assert expected == actual
