from collections import deque


class Solution:
    def shortestPath(
        self, edges: list[list[int]], n: int, m: int, src: int
    ) -> list[int]:
        """
        NOTE:
        time complexity: O(n + m), space complexity: O(n)
        ref: https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph-having-unit-distance/1
        """
        graph: dict[int, list[int]] = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = [edge[1]]
            else:
                graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = [edge[0]]
            else:
                graph[edge[1]].append(edge[0])
        distances: list[int] = [float("inf")] * n
        distances[src] = 0
        visited: set[int] = set()
        visited.add(src)
        queue: deque[tuple[int, int]] = deque([(src, 0)])
        while len(queue) > 0:
            node, accu_dis = queue.popleft()
            accu_dis += 1
            distances[node] = min(distances[node], accu_dis)
            visited.add(node)
            if node not in graph:
                continue
            for next_node in graph[node]:
                if next_node in visited:
                    continue
                queue.append((next_node, distances[node]))
        ## NOTE: It works as well
        # for i in range(len(distances)):
        #     if distances[i] == float("inf"):
        #         distances[i] = -1
        return [-1 if x == float("inf") else x for x in distances]


def test_shortestPath_case_1():
    # arrange
    n: int = 9
    m: int = 10
    edges: list[list[int]] = [
        [0, 1],
        [0, 3],
        [3, 4],
        [4, 5],
        [5, 6],
        [1, 2],
        [2, 6],
        [6, 7],
        [7, 8],
        [6, 8],
    ]
    src: int = 0
    expected: list[list[int]] = [0, 1, 2, 1, 2, 3, 3, 4, 4]

    # act
    solution = Solution()
    actual = solution.shortestPath(edges, n, m, src)

    # assert
    assert expected == actual


def test_shortestPath_case_2():
    # arrange
    n: int = 4
    m: int = 4
    edges: list[list[int]] = [[0, 0], [1, 1], [1, 3], [3, 0]]
    src: int = 3
    expected: list[list[int]] = [1, 1, -1, 0]

    # act
    solution = Solution()
    actual = solution.shortestPath(edges, n, m, src)

    # assert
    assert expected == actual
