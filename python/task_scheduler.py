from collections import Counter, deque
import heapq
from typing import Deque, Tuple


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        time: int = 0
        cnts: dict[str, int] = Counter(tasks)
        maxHeap: list[int] = [-cnt for cnt in cnts.values()]
        heapq.heapify(maxHeap)

        queue: Deque[Tuple[int, int]] = deque()

        while len(queue) > 0 or len(maxHeap) > 0:
            if len(maxHeap) > 0:
                h: int = heapq.heappop(maxHeap)
                if h + 1 < 0:
                    queue.append((h + 1, time + n))

            if len(queue) > 0 and time >= queue[0][1]:
                q: Tuple[int, int] = queue.popleft()
                heapq.heappush(maxHeap, q[0])

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
