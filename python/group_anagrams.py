class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result: list[list[str]] = list()
        strMap: dict[tuple[int], list[str]] = dict()

        for s in strs:
            count: list[int] = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1

            if tuple(count) not in strMap:
                strMap[tuple(count)] = [s]
            else:
                strMap[tuple(count)].append(s)

        for _, v in strMap.items():
            result.append(v)

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
