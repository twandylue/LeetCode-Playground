from collections import deque
import heapq


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        """time complexity: O(n), space complexity: O(26)"""
        # (time, task, freq)
        queue: deque(tuple[int, str, int]) = deque()
        # (freq, task)
        max_heap: list[tuple[int, str]] = []
        freq_map: dict[str, int] = defaultdict(int)
        for task in tasks:
            freq_map[task] += 1
        for k, v in freq_map.items():
            heapq.heappush(max_heap, (-1 * v, k))
        time: int = 0
        while len(queue) > 0 or len(max_heap) > 0:
            if len(max_heap) > 0:
                freq, task = heapq.heappop(max_heap)
                if freq + 1 < 0:
                    queue.append((time + n, task, freq + 1))
            if len(queue) > 0 and time >= queue[0][0]:
                _, task, freq = queue.popleft()
                heapq.heappush(max_heap, (freq, task))
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
