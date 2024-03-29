from collections import deque


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: list[int], informTime: list[int]
    ) -> int:
        """time complexity: O(n) by using bfs"""
        adj: dict[int, list[int]] = {}
        for i in range(n):
            if manager[i] not in adj:
                adj[manager[i]] = [i]
            else:
                adj[manager[i]].append(i)
        que: deque[tuple[int, int]] = deque([(headID, informTime[headID])])
        result: int = 0
        while len(que) > 0:
            i, time = que.popleft()
            result = max(result, time)
            if i not in adj:
                continue
            for employ in adj[i]:
                que.append((employ, time + informTime[employ]))
        return result


def test_numOfMinutes_case_1():
    """This is a test case"""
    # arrange
    n: int = 1
    headID: int = 0
    manager: list[int] = [-1]
    informTime: list[int] = [0]
    expected: int = 0

    # act
    solution = Solution()
    actual = solution.numOfMinutes(n, headID, manager, informTime)

    # assert
    assert expected == actual


def test_numOfMinutes_case_2():
    """This is a test case"""
    # arrange
    n: int = 6
    headID: int = 2
    manager: list[int] = [2, 2, -1, 2, 2, 2]
    informTime: list[int] = [0, 0, 1, 0, 0, 0]
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.numOfMinutes(n, headID, manager, informTime)

    # assert
    assert expected == actual
