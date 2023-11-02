class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result: list[list[int]] = list()
        intervals.sort()
        mergedInterval: list[int] = intervals[0]

        for i in range(0, len(intervals)):
            if mergedInterval[1] >= intervals[i][0]:
                mergedInterval[1] = max(mergedInterval[1], intervals[i][1])
            else:
                result.append(mergedInterval)
                mergedInterval: list[int] = [intervals[i][0], intervals[i][1]]

        result.append(mergedInterval)
        return result


def test_insert_case_1():
    # arrange
    intervals: list[list[int]] = [[1, 3], [2, 6], [8, 10], [15, 18]]
    expected: list[list[int]] = [[1, 6], [8, 10], [15, 18]]

    # act
    solution = Solution()
    actual = solution.merge(intervals)

    # assert
    assert expected == actual


def test_insert_case_2():
    # arrange
    intervals: list[list[int]] = [[1, 4], [0, 4]]
    expected: list[list[int]] = [[0, 4]]

    # act
    solution = Solution()
    actual = solution.merge(intervals)

    # assert
    assert expected == actual


def test_insert_case_3():
    # arrange
    intervals: list[list[int]] = [[1, 4], [0, 0]]
    expected: list[list[int]] = [[0, 0], [1, 4]]

    # act
    solution = Solution()
    actual = solution.merge(intervals)

    # assert
    assert expected == actual
