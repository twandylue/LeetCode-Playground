class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        result: list[int] = []
        visited: set[int] = set()
        cycle: set[int] = set()
        course_graph: dict[int, list[int]] = dict()

        for item in prerequisites:
            course: int = item[0]
            pre: int = item[1]
            if course in course_graph:
                course_graph[course].append(pre)
            else:
                course_graph[course] = [pre]

        for c in range(0, numCourses):
            if self.dfs(c, visited, cycle, result, course_graph):
                continue
            return []

        return result

    def dfs(
        self,
        course: int,
        visited: set[int],
        cycle: set[int],
        result: list[int],
        course_graph: dict[int, list[int]],
    ) -> bool:
        if course in visited:
            return True
        if course in cycle:
            return False

        cycle.add(course)
        if course in course_graph:
            for pre in course_graph[course]:
                if self.dfs(pre, visited, cycle, result, course_graph):
                    continue
                return False

        cycle.remove(course)
        visited.add(course)
        result.append(course)

        return True


def test_findOrder_case_1():
    # arrange
    numCourses: int = 2
    prerequisites: list[list[int]] = [[1, 0]]
    expected: list[int] = [0, 1]

    # act
    solution = Solution()
    actual: list[int] = solution.findOrder(numCourses, prerequisites)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_findOrder_case_2():
    # arrange
    numCourses: int = 4
    prerequisites: list[list[int]] = [[1, 0], [2, 0], [3, 1], [3, 2]]
    expected: list[int] = [0, 2, 1, 3]

    # act
    solution = Solution()
    actual: list[int] = solution.findOrder(numCourses, prerequisites)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual


def test_findOrder_case_3():
    # arrange
    numCourses: int = 1
    prerequisites: list[list[int]] = []
    expected: list[int] = [0]

    # act
    solution = Solution()
    actual: list[int] = solution.findOrder(numCourses, prerequisites)

    # assert
    expected.sort()
    actual.sort()
    assert expected == actual
