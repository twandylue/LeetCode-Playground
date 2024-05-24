from collections import deque


class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        visited: set[str] = set(deadends)
        queue: deque[tuple[str, int]] = deque([("0000", 0)])
        while len(queue) > 0:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for neighbor in self.children(lock):
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                queue.append((neighbor, turns + 1))
        return -1

    def children(self, lock: str) -> list[str]:
        result: list[str] = []
        for i in range(4):
            digit: str = str((int(lock[i]) + 1) % 10)
            result.append(lock[:i] + digit + lock[i + 1 :])
            digit = str((int(lock[i]) - 1 + 10) % 10)
            result.append(lock[:i] + digit + lock[i + 1 :])
        return result


def test_openLock_case_1():
    # arrange
    deadends: list[str] = ["0201", "0101", "0102", "1212", "2002"]
    target: str = "0202"
    expected: int = 6

    # act
    solution = Solution()
    actual = solution.openLock(deadends, target)

    # assert
    assert expected == actual


def test_openLock_case_2():
    # arrange
    deadends: list[str] = ["8888"]
    target: str = "0009"
    expected: int = 1

    # act
    solution = Solution()
    actual = solution.openLock(deadends, target)

    # assert
    assert expected == actual


def test_openLock_case_3():
    # arrange
    deadends: list[str] = [
        "8887",
        "8889",
        "8878",
        "8898",
        "8788",
        "8988",
        "7888",
        "9888",
    ]
    target: str = "8888"
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.openLock(deadends, target)

    # assert
    assert expected == actual
