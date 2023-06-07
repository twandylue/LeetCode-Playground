class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        mertedList: list[int] = []
        for m in matrix:
            mertedList.extend(m)

        l: int = 0
        r: int = len(mertedList) - 1
        while l <= r:
            mid: int = int((l + r) / 2)
            if mertedList[mid] == target:
                return True
            elif mertedList[mid] > target:
                r = mid - 1
            elif mertedList[mid] < target:
                l = mid + 1

        return False


def test_searchMatrix_case_1():
    # arrange
    matrix: list[list[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target: int = 3
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.searchMatrix(matrix, target)

    # assert
    assert actual == expected


def test_searchMatrix_case_2():
    # arrange
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    expected = False

    # act
    solution = Solution()
    actual = solution.searchMatrix(matrix, target)

    # assert
    assert actual == expected


def test_searchMatrix_case_3():
    # arrange
    matrix = [[1, 3]]
    target = 3
    expected = True

    # act
    solution = Solution()
    actual = solution.searchMatrix(matrix, target)

    # assert
    assert actual == expected
