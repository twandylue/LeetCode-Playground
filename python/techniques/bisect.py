def bisect_left(nums: list[int], target: int) -> int:
    l: int = 0
    r: int = len(nums)
    while l < r:
        mid: int = l + (r - l) // 2
        if nums[mid] >= target:
            r = mid
        else:
            l = mid + 1
    return l

def bisect_right(nums: list[int] , target: int) -> int:
    l: int = 0
    r: int = len(nums)
    while l < r:
        mid: int = l + (r - l) // 2
        if nums[mid] > target:
            r = mid
        else:
            l = mid + 1
    return l
