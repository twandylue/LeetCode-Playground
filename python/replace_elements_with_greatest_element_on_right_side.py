class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        result: list[int] = [0] * (len(arr) + 1)
        result[-1] = -1
        for i in reversed(range(len(arr))):
            result[i] = max(arr[i], result[i + 1])

        return result[1::]


def test_replaceElements_case_1():
    # arrange
    arr: list[int] = [17, 18, 5, 4, 6, 1]
    expected: list[int] = [18, 6, 6, 6, 1, -1]

    # act
    solution = Solution()
    actual = solution.replaceElements(arr)

    # assert
    assert expected == actual


def test_replaceElements_case_2():
    # arrange
    arr: list[int] = [400]
    expected: list[int] = [-1]

    # act
    solution = Solution()
    actual = solution.replaceElements(arr)

    # assert
    assert expected == actual
