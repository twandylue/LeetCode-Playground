class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums: list[int] = [int(x) for x in str(n)]
        for i in reversed(range(len(nums) - 1)):
            if nums[i] >= nums[i + 1]:
                continue

            j: int = i + 1
            while j < len(nums):
                if nums[j] <= nums[i]:
                    j = j - 1
                    break
                j += 1

            if j == len(nums):
                j = len(nums) - 1

            tmp: int = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            nums[i + 1 :] = sorted(nums[i + 1 :])

            strN: list[str] = [str(x) for x in nums]
            result: int = int("".join(strN))
            if result > 2147483647:
                return -1

            return result

        return -1


def test_nextGreaterElement_case_1():
    # arrange
    n: int = 12
    expected: int = 21

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(n)

    # assert
    assert expected == actual


def test_nextGreaterElement_case_2():
    # arrange
    n: int = 21
    expected: int = -1

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(n)

    # assert
    assert expected == actual


def test_nextGreaterElement_case_3():
    # arrange
    n: int = 101
    expected: int = 110

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(n)

    # assert
    assert expected == actual


def test_nextGreaterElement_case_4():
    # arrange
    n: int = 230241
    expected: int = 230412

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(n)

    # assert
    assert expected == actual


def test_nextGreaterElement_case_5():
    # arrange
    n: int = 2147483476
    expected: int = 2147483647

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(n)

    # assert
    assert expected == actual


def test_nextGreaterElement_case_6():
    # arrange
    n: int = 12443322
    expected: int = 13222344

    # act
    solution = Solution()
    actual = solution.nextGreaterElement(n)

    # assert
    assert expected == actual
