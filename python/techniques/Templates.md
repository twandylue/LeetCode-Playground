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

## Segment Tree Template

```python
class NumArray:

    def __init__(self, nums: List[int]):
        self.n: int = len(nums)
        self.tree: list[int] = [0] * 4 * self.n
        self._build(1, 0, self.n - 1, nums)

    def _build(self, node: int, s: int, e: int, nums: list[int]) -> None:
        if s == e:
            self.tree[node] = nums[s]
            return
        mid: int = (s + e) // 2
        self._build(node * 2, s, mid, nums)
        self._build(node * 2 + 1, mid + 1, e, nums)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def update(self, index: int, val: int) -> None:
        self._update(1, 0, self.n - 1, index, val)

    def _update(self, node: int, s: int, e: int, index: int, val: int) -> None:
        if s == e:
            self.tree[node] = val
            return
        mid: int = (s + e) // 2
        if index <= mid:
            self._update(node * 2, s, mid, index, val)
        else:
            self._update(node * 2 + 1, mid + 1, e, index, val)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]

    def sumRange(self, left: int, right: int) -> int:
        return self._query(1, 0, self.n - 1, left, right)

    def _query(self, node: int, s: int, e: int, left: int, right: int) -> int:
        if left > e or right < s:
            return 0
        if left <= s and e <= right:
            return self.tree[node]
        mid: int = (s + e) // 2
        return self._query(node * 2, s, mid, left, right) + self._query(
            node * 2 + 1, mid + 1, e, left, right
        )
```

