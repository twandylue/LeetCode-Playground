def binarySearch_lower_bound(nums: list[int], target: int) -> int:
    """
    find the lower bound of the target in the nums list
    Input:
    [1,2,3,4,6,6,8,11]
    6

    Output:
    4
    """
    l: int = 0
    r: int = len(nums) - 1
    while l < r:
        mid: int = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l


def binarySearch_upper_bound(nums: list[int], target: int) -> int:
    """
    find the upper bound of the target in the nums list
    Input:
    [1,2,3,4,6,6,8,11]
    6

    Output:
    6
    """
    l: int = 0
    r: int = len(nums) - 1
    while l < r:
        mid: int = (l + r) // 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l
