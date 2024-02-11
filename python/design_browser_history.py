"""for Optional"""
from typing import Optional


class Node:
    def __init__(
        self,
        val: str,
        prev: Optional["Node"] = None,
        next_node: Optional["Node"] = None,
    ):
        self.val = val
        self.prev = prev
        self.next = next_node


class BrowserHistory:
    def __init__(self, homepage: str):
        home_node: Node = Node(homepage)
        self.head = Node("head")
        self.tail = Node("tail")
        self.head.next = home_node
        home_node.prev = self.head
        home_node.next = self.tail
        self.tail.prev = home_node
        self.curr = home_node

    def visit(self, url: str) -> None:
        """time complexit: O(1)"""
        new_node: Node = Node(url)
        self.curr.next = new_node
        new_node.prev = self.curr
        new_node.next = self.tail
        self.tail.prev = new_node
        self.curr = new_node

    def back(self, steps: int) -> str:
        """time complexit: O(n)"""
        idx: int = 0
        while idx < steps and self.curr is not None:
            if self.curr.prev == self.head:
                break
            idx += 1
            self.curr = self.curr.prev

        if self.curr is None:
            raise Exception("impossible")

        return self.curr.val

    def forward(self, steps: int) -> str:
        """time complexit: O(n)"""
        idx: int = 0
        while idx < steps and self.curr is not None:
            if self.curr.next == self.tail:
                break
            idx += 1
            self.curr = self.curr.next

        if self.curr is None:
            raise Exception("impossible")

        return self.curr.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
def test_browser_history_case_1():
    """test case"""
    browser_history: BrowserHistory = BrowserHistory("leetcode.com")
    browser_history.visit("google.com")  # You are in "leetcode.com". Visit "google.com"
    browser_history.visit(
        "facebook.com"
    )  # You are in "google.com". Visit "facebook.com"
    browser_history.visit(
        "youtube.com"
    )  # You are in "facebook.com". Visit "youtube.com"
    actual1: str = browser_history.back(
        1
    )  # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    actual2: str = browser_history.back(
        1
    )  # You are in "facebook.com", move back to "google.com" return "google.com"
    actual3: str = browser_history.forward(
        1
    )  # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    browser_history.visit(
        "linkedin.com"
    )  # You are in "facebook.com". Visit "linkedin.com"
    actual4: str = browser_history.forward(
        2
    )  # You are in "linkedin.com", you cannot move forward any steps.
    actual5: str = browser_history.back(
        2
    )  # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    actual6: str = browser_history.back(
        7
    )  # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"

    assert actual1 == "facebook.com"
    assert actual2 == "google.com"
    assert actual3 == "facebook.com"
    assert actual4 == "linkedin.com"
    assert actual5 == "google.com"
    assert actual6 == "leetcode.com"
