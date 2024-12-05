class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        """time complexity: O(nlogn)"""
        intervals.sort()
        for i in range(len(intervals) - 1):
            if intervals[i][1] > intervals[i + 1][0]:
                return False
        return True


def test_canAttendMeetings_case_1():
    # arrange
    intervals: list[list[int]] = [[0, 30], [5, 10], [15, 20]]
    expected: bool = False

    # act
    actual = Solution().canAttendMeetings(intervals)

    # assert
    assert expected == actual


def test_canAttendMeetings_case_2():
    # arrange
    intervals: list[list[int]] = [[7, 10], [2, 4]]
    expected: bool = True

    # act
    actual = Solution().canAttendMeetings(intervals)

    # assert
    assert expected == actual
