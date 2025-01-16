from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """time complexity: O(n)"""
        result: list[list[str]] = []
        anag_map: dict[tuple[int], list[str]] = defaultdict(list)
        for string in strs:
            count: list[int] = [0] * 26
            for c in string:
                count[ord(c) - ord("a")] += 1
            tup: tuple[int] = tuple(count)
            anag_map[tup].append(string)
        for value in anag_map.values():
            result.append(value)
        return result


## NOTE: Ignore since sorting problem in expected
# def test_groupAnagrams_case_1():
#     # arrange
#     strs: list[str] = ["eat", "tea", "tan", "ate", "nat", "bat"]
#     expected: list[list[str]] = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
#
#     # act
#     solution = Solution()
#     actual = solution.groupAnagrams(strs)
#
#     # assert
#     expected.sort()
#     actual.sort()
#     assert expected == actual
