class Solution:
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        l: int = 0
        r: int = 1
        result: int = 1
        prev: str = ""
        while l < r and r < len(arr):
            if arr[r - 1] > arr[r] and prev != ">":
                result = max(result, r - l + 1)
                prev = ">"
                r += 1
            elif arr[r - 1] < arr[r] and prev != "<":
                result = max(result, r - l + 1)
                prev = "<"
                r += 1
            elif arr[r - 1] == arr[r]:
                l = r
                r += 1
                prev = ""
            else:
                prev = ""
                l = r - 1

        return result


def test_maxTurbulenceSize_case_1():
    # arrange
    arr: list[int] = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    expected: int = 5

    # act
    solution = Solution()
    actual = solution.maxTurbulenceSize(arr)

    # assert
    assert expected == actual


def test_maxTurbulenceSize_case_2():
    # arrange
    arr: list[int] = [4, 8, 12, 16]
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.maxTurbulenceSize(arr)

    # assert
    assert expected == actual


def test_maxTurbulenceSize_case_3():
    # arrange
    arr: list[int] = [100]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.maxTurbulenceSize(arr)

    # assert
    assert expected == actual


def test_maxTurbulenceSize_case_4():
    # arrange
    arr: list[int] = [2, 0, 2, 4, 2, 5, 0, 1, 2, 3]
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.maxTurbulenceSize(arr)

    # assert
    assert expected == actual
