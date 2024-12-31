from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        graph: dict[int, list[int]] = {}
        for i in range(numCourses):
            if i not in graph:
                graph[i] = []
        for pre, course in prerequisites:
            if course not in graph:
                graph[course] = [pre]
            else:
                graph[course].append(pre)
        pre_map: dict[int, set[int]] = {}
        for i in range(numCourses):
            self.dfs(i, pre_map, graph)
        result: list[bool] = []
        for f, s in queries:
            if s in pre_map:
                result.append(f in pre_map[s])
            else:
                result.append(False)
        return result

    def dfs(
        self, course: int, pre_map: dict[int, set[int]], graph: dict[int, list[int]]
    ) -> set[int]:
        if course not in pre_map:
            pre_map[course] = set()
            for pre in graph[course]:
                pre_map[course] |= self.dfs(pre, pre_map, graph)  # union
            pre_map[course].add(course)
        return pre_map[course]

    def checkIfPrerequisite2(
        self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]
    ) -> list[bool]:
        """
        time complexity: O(N + E + Q)
        space complexity: O(N^2)
        Topological sort
        """
        adj: dict[int, list[int]] = defaultdict(list)
        reachable: list[list[bool]] = [[False] * numCourses for _ in range(numCourses)]
        indegree: list[int] = [0] * numCourses
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        queue: deque[int] = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                queue.append(i)
        while len(queue) > 0:
            course: int = queue.popleft()
            for nei in adj[course]:
                reachable[course][nei] = True
                for i in range(numCourses):
                    if reachable[i][course]:
                        reachable[i][nei] = True
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        result: list[bool] = []
        for query in queries:
            result.append(reachable[query[0]][query[1]])
        return result


def test_checkIfPrerequisite_case_1():
    # arrange
    numCourses: int = 2
    prerequisites: list[list[int]] = [[1, 0]]
    queries: list[list[int]] = [[0, 1], [1, 0]]
    expected: list[bool] = [False, True]

    # act
    solution = Solution()
    actual = solution.checkIfPrerequisite(numCourses, prerequisites, queries)

    # assert
    assert expected == actual


def test_checkIfPrerequisite_case_2():
    # arrange
    numCourses: int = 2
    prerequisites: list[int] = []
    queries: list[list[int]] = [[1, 0], [0, 1]]
    expected: list[bool] = [False, False]

    # act
    solution = Solution()
    actual = solution.checkIfPrerequisite(numCourses, prerequisites, queries)

    # assert
    assert expected == actual


def test_checkIfPrerequisite_case_3():
    # arrange
    numCourses: int = 2
    prerequisites: list[int] = []
    queries: list[list[int]] = [[1, 0], [0, 1]]
    expected: list[bool] = [False, False]

    # act
    actual = Solution().checkIfPrerequisite2(numCourses, prerequisites, queries)

    # assert
    assert expected == actual
