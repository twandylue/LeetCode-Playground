class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        l: int = 0
        numsSet: set[int] = set()
        for r in range(len(nums)):
            if r - l > k:
                numsSet.remove(nums[l])
                l += 1
            if nums[r] in numsSet:
                return True

            numsSet.add(nums[r])
        return False


def test_containsNearbyDuplicate_case_1():
    # arrange
    nums: list[int] = [1, 2, 3, 1]
    k: int = 3
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.containsNearbyDuplicate(nums, k)

    # assert
    assert expected == actual


def test_containsNearbyDuplicate_case_2():
    # arrange
    nums: list[int] = [1, 0, 1, 1]
    k: int = 1
    expected: bool = True

    # act
    solution = Solution()
    actual = solution.containsNearbyDuplicate(nums, k)

    # assert
    assert expected == actual


def test_containsNearbyDuplicate_case_3():
    # arrange
    nums: list[int] = [1, 2, 3, 1, 2, 3]
    k: int = 2
    expected: bool = False

    # act
    solution = Solution()
    actual = solution.containsNearbyDuplicate(nums, k)

    # assert
    assert expected == actual
