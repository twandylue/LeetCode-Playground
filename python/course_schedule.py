class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        courseCache: dict[int, list[int]] = dict()
        visited: dict[int, int] = dict()

        for item in prerequisites:
            course = item[0]
            pre = item[1]
            if course not in courseCache:
                courseCache[course] = [pre]
            else:
                courseCache[course].append(pre)

        for c in range(0, numCourses):
            if self.dfs(c, visited, courseCache):
                continue
            return False

        return True

    def dfs(
        self, course: int, visited: dict[int, int], courseCache: dict[int, list[int]]
    ) -> bool:
        if course not in courseCache:
            return True

        if course in visited:
            if visited[course] == 1:
                return False
            elif visited[course] == 0:
                return True

        visited[course] = 1
        for pre in courseCache[course]:
            if self.dfs(pre, visited, courseCache):
                continue
            return False

        visited[course] = 0
        return True


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
