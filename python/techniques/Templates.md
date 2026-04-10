# Templates

## Binary Search Template

```python
def binary_search(array) -> int:
    def condition(value) -> bool:
        pass

    left, right = min(search_space), max(search_space) # could be [0, n], [1, n] etc. Depends on problem
    while left < right:
        mid = left + (right - left) // 2
        if condition(mid):
            right = mid
        else:
            left = mid + 1
    return left
```

ref: [Binary Search Template](https://leetcode.com/discuss/post/786126/python-powerful-ultimate-binary-search-t-rwv8/)


```python
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
```

## Kth-smallest Heap Template

```python
def kth_smallest_heap -> int:
    max_heap: list[int] = []
    for i in ragne(len(matrix)):
        for j in range(len(matrix[i])):
            heapq.heappush(max_heap, -1 * matrix[i][j])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
    return -1 * max_heap[0] # kth-smallest in the matrix
```

## Is Prime Template

```python
def is_prime(val: int) -> bool:
    if val == 1:
        return False
    if val == 2:
        return True
    l: int = 1
    r: int = val
    while l < r:
        mid: int = l + (r - l) // 2
        if mid != 1 and val % mid == 0:
            return False
        else:
            r = mid
    return r != 1
```

