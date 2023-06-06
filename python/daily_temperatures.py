class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        output: list[int] = [0] * len(temperatures)
        stack: list[int] = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                output[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return output


def test_dailyTemperatures_case_1():
    # arrange
    temperatures: list[int] = [73, 74, 75, 71, 69, 72, 76, 73]
    expected: list[int] = [1, 1, 4, 2, 1, 1, 0, 0]

    # act
    solution = Solution()
    actual = solution.dailyTemperatures(temperatures)

    # assert
    assert actual == expected


def test_dailyTemperatures_case_2():
    # arrange
    temperatures: list[int] = [30, 40, 50, 60]
    expected: list[int] = [1, 1, 1, 0]

    # act
    solution = Solution()
    actual = solution.dailyTemperatures(temperatures)

    # assert
    assert actual == expected


def test_dailyTemperatures_case_3():
    # arrange
    temperatures: list[int] = [30, 60, 90]
    expected: list[int] = [1, 1, 0]

    # act
    solution = Solution()
    actual = solution.dailyTemperatures(temperatures)

    # assert
    assert actual == expected
