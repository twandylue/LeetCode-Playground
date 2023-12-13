class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        result: list[set] = [set(), set()]
        nums1Set: set[int] = set(nums1)
        nums2Set: set[int] = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] not in nums2Set:
                result[0].add(nums1[i])
        for i in range(len(nums2)):
            if nums2[i] not in nums1Set:
                result[1].add(nums2[i])

        return [list(result[0]), list(result[1])]


def test_findDifference_case_1():
    # arrange
    nums1: list[int] = [1, 2, 3]
    nums2: list[int] = [2, 4, 6]
    expected: list[list[int]] = [[1, 3], [4, 6]]

    # act
    solution = Solution()
    actual = solution.findDifference(nums1, nums2)

    # assert
    assert expected == actual


def test_findDifference_case_2():
    # arrange
    nums1: list[int] = [1, 2, 3, 3]
    nums2: list[int] = [1, 1, 2, 2]
    expected: list[list[int]] = [[3], []]

    # act
    solution = Solution()
    actual = solution.findDifference(nums1, nums2)

    # assert
    assert expected == actual
