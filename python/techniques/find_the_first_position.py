# NOTE: LC. 34. Find First and Last Position of Element in Sorted Array
def binarySearch(nums: list[int], target: int, isLeft: bool) -> int:
    l: int = 0
    r: int = len(nums) - 1
    result: int = -1
    while l <= r:
        mid: int = (l + r) // 2
        if nums[mid] == target:
            result = mid
            if isLeft:
                r = mid - 1
            else:
                l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1

    return result
