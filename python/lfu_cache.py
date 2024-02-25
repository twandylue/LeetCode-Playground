from typing import Optional


class ListNode:
    def __init__(
        self,
        key: int = 0,
        value: int = 0,
        prev: Optional["ListNode"] = None,
        next_node: Optional["ListNode"] = None,
    ):
        self.val = value
        self.key = key
        self.prev: Optional["ListNode"] = prev
        self.next: Optional["ListNode"] = next_node


class LinkedList:
    """doubly linked list."""

    def __init__(self):
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right
        self.right.prev = self.left
        self.node_map: dict[int, ListNode] = {}

    def length(self) -> int:
        """get the length of the linked list. time complexity: O(1)"""
        return len(self.node_map)

    def get(self, key: int) -> Optional[ListNode]:
        """get the node by key. time complexity: O(1)"""
        if key not in self.node_map:
            return None
        return self.node_map[key]

    def pop(self) -> Optional[ListNode]:
        """pop the last node. time complexity: O(1)"""
        last_node: Optional[ListNode] = self.right.prev
        if last_node == self.left or last_node is None:
            return None
        self.remove(last_node)
        return last_node

    def insert_after_head(self, node: ListNode) -> None:
        """insert the node after the head. time complexity: O(1)"""
        if node is None:
            return
        node.next = self.left.next
        node.prev = self.left
        self.left.next.prev = node
        self.left.next = node
        self.node_map[node.key] = node

    def remove(self, node: ListNode) -> None:
        """remove the node. time complexity: O(1)"""
        if node is None or node.key not in self.node_map:
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.node_map.pop(node.key)


class LFUCache:
    """LFU Cache."""

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.value_map: dict[int, int] = {}
        self.counter_map: dict[int, int] = {}
        self.count_list_map: dict[int, LinkedList] = {}
        self.lfu_count: int = 0

    def get(self, key: int) -> int:
        """get the value by key. time complexity: O(1)"""
        if key not in self.value_map or key not in self.counter_map:
            return -1
        count: int = self.counter_map[key]
        linked_list: LinkedList = self.count_list_map[count]
        node: Optional[ListNode] = linked_list.get(key)
        linked_list.remove(node)
        if linked_list.length() == 0:
            self.count_list_map.pop(count)
            if count == self.lfu_count:
                self.lfu_count += 1
        self.counter_map[key] = count + 1
        if count + 1 not in self.count_list_map:
            new_linked_list: LinkedList = LinkedList()
            new_linked_list.insert_after_head(node)
            self.count_list_map[count + 1] = new_linked_list
        else:
            linked_list: LinkedList = self.count_list_map[count + 1]
            linked_list.insert_after_head(node)

        return self.value_map[key]

    def put(self, key: int, value: int) -> None:
        """put the value by key. time complexity: O(1)"""
        if self.capacity == 0:
            return

        if key in self.value_map:
            self.value_map[key] = value
            count: int = self.counter_map[key]
            self.counter_map[key] = count + 1
            linked_list: LinkedList = self.count_list_map[count]
            updated_node: Optional[ListNode] = linked_list.get(key)
            linked_list.remove(updated_node)
            if linked_list.length() == 0:
                self.count_list_map.pop(count)
                if count == self.lfu_count:
                    self.lfu_count += 1
            if count + 1 not in self.count_list_map:
                new_linked_list: LinkedList = LinkedList()
                new_linked_list.insert_after_head(updated_node)
                self.count_list_map[count + 1] = new_linked_list
            else:
                linked_list: LinkedList = self.count_list_map[count + 1]
                linked_list.insert_after_head(updated_node)
            return

        if key not in self.value_map and len(self.value_map) == self.capacity:
            linked_list: LinkedList = self.count_list_map[self.lfu_count]
            lfu_node: Optional[ListNode] = linked_list.pop()
            if linked_list.length() == 0:
                self.count_list_map.pop(self.lfu_count)
                self.lfu_count += 1
            self.value_map.pop(lfu_node.key)
            self.counter_map.pop(lfu_node.key)
        new_node: ListNode = ListNode(key, value)
        self.value_map[key] = value
        self.counter_map[key] = 1
        self.lfu_count = 1
        if 1 not in self.count_list_map:
            new_linked_list: LinkedList = LinkedList()
            new_linked_list.insert_after_head(new_node)
            self.count_list_map[1] = new_linked_list
        else:
            linked_list: LinkedList = self.count_list_map[1]
            linked_list.insert_after_head(new_node)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
def test_lfu_case1():
    """test case 1"""
    # Your LRUCache object will be instantiated and called as such:
    # obj = LRUCache(capacity)
    # param_1 = obj.get(key)
    # obj.put(key,value)
    lfu_cache: LFUCache = LFUCache(2)
    lfu_cache.put(1, 1)  # cache=[1,_], cnt(1)=1
    lfu_cache.put(2, 2)  # cache=[2,1], cnt(2)=1, cnt(1)=1
    actual1 = lfu_cache.get(1)  # return 1, cache=[1,2], cnt(2)=1, cnt(1)=2
    lfu_cache.put(
        3, 3
    )  # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2. cache=[3,1], cnt(3)=1, cnt(1)=2
    actual2 = lfu_cache.get(2)  # returns -1 (not found)
    actual3 = lfu_cache.get(3)  # returns 3, cache=[3,1], cnt(3)=2, cnt(1)=2
    lfu_cache.put(
        4, 4
    )  # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1. cache=[4,3], cnt(4)=1, cnt(3)=2
    actual4 = lfu_cache.get(1)  # returns -1 (not found)
    actual5 = lfu_cache.get(3)  # return 3, cache=[3,4], cnt(4)=1, cnt(3)=3
    actual6 = lfu_cache.get(4)  # return 4, cache=[4,3], cnt(4)=2, cnt(3)=3

    assert actual1 == 1
    assert actual2 == -1
    assert actual3 == 3
    assert actual4 == -1
    assert actual5 == 3
    assert actual6 == 4
