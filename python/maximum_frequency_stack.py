class FreqStack:
    def __init__(self):
        self.countMap: dict[int, int] = dict()  # number, counts
        self.groupMap: dict[int, list[int]] = dict()  # counts, list[number]
        self.maxCount: int = 0

    def push(self, val: int) -> None:
        if val not in self.countMap:
            self.countMap[val] = 1
        else:
            self.countMap[val] += 1

        self.maxCount = max(self.maxCount, self.countMap[val])

        if self.countMap[val] not in self.groupMap:
            self.groupMap[self.countMap[val]] = [val]
        else:
            self.groupMap[self.countMap[val]].append(val)

    def pop(self) -> int:
        maxCountVal: int = 0
        if len(self.groupMap[self.maxCount]) > 0:
            maxCountVal = self.groupMap[self.maxCount].pop()
            if maxCountVal in self.countMap:
                self.countMap[maxCountVal] -= 1
        if len(self.groupMap[self.maxCount]) == 0:
            self.maxCount -= 1

        return maxCountVal


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
def test_FreqStack_case_1():
    # arrange
    freqStack = FreqStack()
    expected1: int = 5
    expected2: int = 7
    expected3: int = 5
    expected4: int = 4

    # act
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(5)
    freqStack.push(7)
    freqStack.push(4)
    freqStack.push(5)
    actual1: int = freqStack.pop()
    actual2: int = freqStack.pop()
    actual3: int = freqStack.pop()
    actual4: int = freqStack.pop()

    # assert
    assert actual1 == expected1
    assert actual2 == expected2
    assert actual3 == expected3
    assert actual4 == expected4
