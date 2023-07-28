from collections import deque
from typing import Deque


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def walls_and_gates(self, rooms: list[list[int]]):
        queue: Deque[tuple[int, int]] = deque()
        visited: set[tuple[int, int]] = set()
        for r in range(len(rooms)):
            for c in range(len(rooms[0])):
                if rooms[r][c] == 0:
                    queue.append((r, c))
                    visited.add((r, c))

        distance: int = 0
        while len(queue) > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                rooms[r][c] = distance
                self.walkRoom(r + 1, c, visited, queue, rooms)
                self.walkRoom(r - 1, c, visited, queue, rooms)
                self.walkRoom(r, c + 1, visited, queue, rooms)
                self.walkRoom(r, c - 1, visited, queue, rooms)

            distance += 1

        return

    def walkRoom(
        self,
        row: int,
        col: int,
        visited: set[tuple[int, int]],
        queue: deque[tuple[int, int]],
        rooms: list[list[int]],
    ) -> None:
        if (
            row < 0
            or row >= len(rooms)
            or col < 0
            or col >= len(rooms[0])
            or (row, col) in visited
            or rooms[row][col] == -1
        ):
            return

        visited.add((row, col))
        queue.append((row, col))


def test_calls_and_gates_case_1():
    # arrange
    rooms: list[list[int]] = [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]

    expected: list[list[int]] = [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]

    # act
    solution = Solution()
    solution.walls_and_gates(rooms)

    # assert
    assert expected == rooms


def test_calls_and_gates_case_2():
    # arrange
    rooms: list[list[int]] = [[0, -1], [2147483647, 2147483647]]

    expected: list[list[int]] = [[0, -1], [1, 2]]

    # act
    solution = Solution()
    solution.walls_and_gates(rooms)

    # assert
    assert expected == rooms
