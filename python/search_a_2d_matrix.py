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

    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        l: int = 0
        r: int = len(matrix[0]) - 1
        bot: int = 0
        top: int = len(matrix) - 1
        while bot <= top:
            row: int = (bot + top) // 2
            if target > matrix[row][r]:
                bot = row + 1
            elif target < matrix[row][l]:
                if row > 0:
                    top = row - 1
                else:
                    break
            else:
                break

        if bot > top:
            return False
        row: int = (bot + top) // 2

        while l <= r:
            mid: int = (l + r) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                if mid > 0:
                    r = mid - 1
                else:
                    break
            elif target > matrix[row][mid]:
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


def test_searchMatrix_case_4():
    # arrange
    matrix: list[list[int]] = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target: int = 3
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.searchMatrix2(matrix, target)

    # assert
    assert actual == expected


def test_searchMatrix_case_5():
    # arrange
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    expected = False

    # act
    solution = Solution()
    actual = solution.searchMatrix2(matrix, target)

    # assert
    assert actual == expected


def test_searchMatrix_case_6():
    # arrange
    matrix = [[1, 3]]
    target = 3
    expected = True

    # act
    solution = Solution()
    actual = solution.searchMatrix2(matrix, target)

    # assert
    assert actual == expected
