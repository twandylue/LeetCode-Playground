class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        """time: O(n logn)"""
        intervals.sort()
        result: list[list[int]] = [intervals[0]]
        for s, e in intervals:
            last = result[-1][1]
            if s <= last:
                result[-1][1] = max(e, last)
            else:
                result.append([s, e])
        return result

    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        """time: O(n logn)"""
        intervals.sort()
        section: list[int] = intervals[0]
        result: list[list[int]] = []
        for interval in intervals:
            if interval[0] <= section[-1]:
                section[-1] = max(section[-1], interval[-1])
                continue
            result.append(section)
            section = interval
        result.append(section)
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
