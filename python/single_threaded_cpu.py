import heapq


class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        """time complexity: O(nlogn), space complexity: O(n)"""
        result: list[int] = []
        min_heap: list[tuple[int, int]] = []
        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks = sorted(tasks, key=lambda x: x[0])
        i: int = 0
        time: int = tasks[0][0]
        while len(min_heap) > 0 or i < len(tasks):
            while i < len(tasks) and time >= tasks[i][0]:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1
            if len(min_heap) == 0:
                time = tasks[i][0]
            else:
                proce_time, idx = heapq.heappop(min_heap)
                time += proce_time
                result.append(idx)
        return result


def test_getOrder_case_1():
    """This is a test case for getOrder"""
    # arrange
    tasks: list[list[int]] = [[1, 2], [2, 4], [3, 2], [4, 1]]
    expected: list[int] = [0, 2, 3, 1]

    # act
    solution = Solution()
    actual = solution.getOrder(tasks)

    # assert
    assert expected == actual


def test_getOrder_case_2():
    """This is a test case for getOrder"""
    # arrange
    tasks: list[list[int]] = [[7, 10], [7, 12], [7, 5], [7, 4], [7, 2]]
    expected: list[int] = [4, 3, 2, 0, 1]

    # act
    solution = Solution()
    actual = solution.getOrder(tasks)

    # assert
    assert expected == actual


def test_getOrder_case_3():
    """This is a test case for getOrder"""
    # arrange
    tasks: list[list[int]] = [
        [19, 13],
        [16, 9],
        [21, 10],
        [32, 25],
        [37, 4],
        [49, 24],
        [2, 15],
        [38, 41],
        [37, 34],
        [33, 6],
        [45, 4],
        [18, 18],
        [46, 39],
        [12, 24],
    ]
    expected: list[int] = [6, 1, 2, 9, 4, 10, 0, 11, 5, 13, 3, 8, 12, 7]

    # act
    solution = Solution()
    actual = solution.getOrder(tasks)

    # assert
    assert expected == actual
