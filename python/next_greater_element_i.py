class Solution:
    # NOTE: time complexity: O(m * n)
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = [0] * len(nums1)
        nums2Map: dict[int, int] = dict()
        for i in range(len(nums2)):
            if nums2[i] not in nums2Map:
                nums2Map[nums2[i]] = i

        for i in range(len(nums1)):
            isFound: bool = False
            if nums1[i] not in nums2Map:
                return []
            for j in range(nums2Map[nums1[i]], len(nums2)):
                if nums2[j] > nums1[i]:
                    result[i] = nums2[j]
                    isFound = True
                    break
            if not isFound:
                result[i] = -1

        return result

    # NOTE: time complexity: O(m + n)
    def nextGreaterElement2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result: list[int] = [-1] * len(nums1)
        stack: list[int] = list()
        nums1Map: dict[int, int] = dict()

        for i in range(len(nums1)):
            if nums1[i] not in nums1Map:
                nums1Map[nums1[i]] = i

        for i in range(len(nums2)):
            while len(stack) > 0 and stack[-1] < nums2[i]:
                if stack[-1] in nums1Map:
                    result[nums1Map[stack[-1]]] = nums2[i]
                stack.pop()

            stack.append(nums2[i])

        return result


def test_nextGreaterElement_case_1():
    # arrange
    nums1: list[int] = [4, 1, 2]
    nums2: list[int] = [1, 3, 4, 2]
    expected: list[int] = [-1, 3, -1]

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(nums1, nums2)

    # assert
    assert expected == actual


def test_nextGreaterElement_case_2():
    # arrange
    nums1: list[int] = [2, 4]
    nums2: list[int] = [1, 2, 3, 4]
    expected: list[int] = [3, -1]

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(nums1, nums2)

    # assert
    assert expected == actual
