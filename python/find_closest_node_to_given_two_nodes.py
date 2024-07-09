from collections import deque, defaultdict


class Solution:
    def closestMeetingNode(self, edges: list[int], node1: int, node2: int) -> int:
        """time complexity: O(n), where n is the number of edges. space complexity: O(n)"""
        graph: dict[int, list[int]] = defaultdict(list)
        for i in range(len(edges)):
            graph[i].append(edges[i])
        node1_dis_map: dict[int, int] = {}
        node2_dis_map: dict[int, int] = {}
        self.bfs(node1, node1_dis_map, graph)
        self.bfs(node2, node2_dis_map, graph)
        result: int = -1
        min_dis: int = float("inf")
        for i in range(len(edges)):
            if i in node1_dis_map and i in node2_dis_map:
                if min_dis > max(node1_dis_map[i], node2_dis_map[i]):
                    result = i
                    min_dis = max(node1_dis_map[i], node2_dis_map[i])
        return result

    def bfs(self, src: int, dis_map: dict[int, int], graph: dict[int, list[int]]):
        queue: deque[tuple[int, int]] = deque([(src, 0)])
        dis_map[src] = 0
        while len(queue) > 0:
            node, dis = queue.popleft()
            for nei in graph[node]:
                if nei not in dis_map:
                    queue.append((nei, dis + 1))
                    dis_map[nei] = dis + 1


def test_closestMeetingNode_case_1():
    # arrange
    edges: list[int] = [2, 2, 3, -1]
    node1: int = 0
    node2: int = 1
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.closestMeetingNode(edges, node1, node2)

    # assert
    assert expected == actual


def test_closestMeetingNode_case_2():
    # arrange
    edges: list[int] = [1, 2, -1]
    node1: int = 0
    node2: int = 2
    expected: int = 2

    # act
    solution = Solution()
    actual = solution.closestMeetingNode(edges, node1, node2)

    # assert
    assert expected == actual
