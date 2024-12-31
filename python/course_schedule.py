from collections import deque, defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        In short, this question is about detecting cycle in a directed graph. Thus, we have to use a set (visited) and DFS to solve this question.
        Time complexity: O(n + m), where n is the number of courses and m is the number of prerequisites.
        """
        course_graph: dict[int, list[int]] = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            course_graph[course].append(pre)
        visiting_set: set[int] = set()
        completed_set: set[int] = set()
        for c in range(numCourses):
            if self.dfs(c, course_graph, visiting_set, completed_set):
                continue
            return False
        return True

    def dfs(
        self,
        course: int,
        course_graph: dict[int, list[int]],
        visiting_set: set[int],
        completed_set: set[int],
    ) -> bool:
        if course in visiting_set:
            return False
        if course in completed_set:
            return True
        visiting_set.add(course)
        for pre in course_graph[course]:
            if self.dfs(pre, course_graph, visiting_set, completed_set):
                continue
            return False
        completed_set.add(course)
        visiting_set.remove(course)
        return True

    def canFinish2(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        time complexity: O(n + m), space complexity: O(n + m)
        Topological sort using BFS
        """
        indegree: list[int] = [0] * numCourses
        adj: dict[int, list[int]] = defaultdict(list)
        queue: deque[int] = deque()
        for dst, src in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        finish: int = 0
        while len(queue) > 0:
            course: int = queue.popleft()
            finish += 1
            for nei in adj[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)
        return finish == numCourses


def test_canFinish_case_1():
    # arrange
    numCourses: int = 2
    prerequisites: list[list[int]] = [[1, 0]]
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.canFinish(numCourses, prerequisites)

    # assert
    assert expected == actual


def test_canFinish_case_2():
    # arrange
    numCourses: int = 2
    prerequisites: list[list[int]] = [[1, 0], [0, 1]]
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.canFinish(numCourses, prerequisites)

    # assert
    assert expected == actual


def test_canFinish_case_3():
    # arrange
    numCourses: int = 2
    prerequisites: list[list[int]] = [[1, 0], [0, 1]]
    expected: bool = False

    # act
    actual = Solution().canFinish2(numCourses, prerequisites)

    # assert
    assert expected == actual
