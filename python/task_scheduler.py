from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """time complexity: O(n), space complexity: O(26)"""
        time: int = 0
        counter: dict[str, int] = {}
        for task in tasks:
            if task not in counter:
                counter[task] = 1
            else:
                counter[task] += 1
        max_heap: list[int] = []
        for count in counter.values():
            heapq.heappush(max_heap, -count)
        queue: deque[tuple[int, int]] = deque()
        while len(max_heap) > 0 or len(queue) > 0:
            if len(max_heap) > 0:
                h: int = heapq.heappop(max_heap)
                if h + 1 < 0:
                    queue.append((h + 1, time + n))
            if len(queue) > 0 and time >= queue[0][1]:
                c, _ = queue.popleft()
                heapq.heappush(max_heap, c)
            time += 1
        return time


def test_leastInterval_case_1():
    # arrange
    tasks: list[str] = ["A", "A", "A", "B", "B", "B"]
    n: int = 2
    expected: int = 8

    # act
    solution = Solution()
    actual = solution.leastInterval(tasks, n)

    # assert
    assert expected == actual


def test_leastInterval_case_2():
    # arrange
    tasks: list[str] = ["A", "A", "A", "B", "B", "B"]
    n: int = 0
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.leastInterval(tasks, n)

    # assert
    assert expected == actual


def test_leastInterval_case_3():
    # arrange
    tasks: list[str] = ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"]
    n: int = 2
    expected: int = 16

    # act
    solution = Solution()
    actual = solution.leastInterval(tasks, n)

    # assert
    assert expected == actual


def test_leastInterval_case_4():
    # arrange
    tasks: list[str] = ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"]
    n: int = 2
    expected: int = 12

    # act
    solution = Solution()
    actual = solution.leastInterval(tasks, n)

    # assert
    assert expected == actual
