class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        result: list[list[int]] = list()

        for i in range(0, len(intervals)):
            if newInterval[0] > intervals[i][1]:
                result.append(intervals[i])
            elif newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                result.extend(intervals[i:])
                return result
            else:
                newInterval = [
                    min(intervals[i][0], newInterval[0]),
                    max(intervals[i][1], newInterval[1]),
                ]

        result.append(newInterval)

        return result


def test_insert_case_1():
    # arrange
    intervals: list[list[int]] = [[1, 3], [6, 9]]
    newInterval: list[list[int]] = [2, 5]
    expected: list[list[int]] = [[1, 5], [6, 9]]

    # act
    solution = Solution()
    actual = solution.insert(intervals, newInterval)

    # assert
    assert expected == actual


def test_insert_case_2():
    # arrange
    intervals: list[list[int]] = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval: list[list[int]] = [4, 8]
    expected: list[list[int]] = [[1, 2], [3, 10], [12, 16]]

    # act
    solution = Solution()
    actual = solution.insert(intervals, newInterval)

    # assert
    assert expected == actual


def test_insert_case_3():
    # arrange
    intervals: list[list[int]] = []
    newInterval: list[list[int]] = [5, 7]
    expected: list[list[int]] = [[5, 7]]

    # act
    solution = Solution()
    actual = solution.insert(intervals, newInterval)

    # assert
    assert expected == actual
