class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: list[Interval]) -> int:
        """time complexity: O(n logn)"""
        intervals.sort(key=lambda i: i.start)
        min_heap: list[int] = []
        for i in range(len(intervals)):
            if len(min_heap) and min_heap[0].end <= intervals[i].start:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, intervals[i].end)
        return len(min_heap)
