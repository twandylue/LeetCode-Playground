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
        """tiem complexity: O(log(m*n))"""
        top: int = 0
        bot: int = len(matrix) - 1
        target_row: int = 0
        while top <= bot:
            mid_row: int = (top + bot) // 2
            if matrix[mid_row][0] <= target and target <= matrix[mid_row][-1]:
                target_row = mid_row
                break
            if matrix[mid_row][0] > target:
                bot = mid_row - 1
            elif matrix[mid_row][-1] < target:
                top = mid_row + 1
        if top > bot:
            return False
        left: int = 0
        right: int = len(matrix[target_row]) - 1
        while left <= right:
            mid: int = (left + right) // 2
            if matrix[target_row][mid] == target:
                return True
            if matrix[target_row][mid] > target:
                right = mid - 1
            elif matrix[target_row][mid] < target:
                left = mid + 1
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
