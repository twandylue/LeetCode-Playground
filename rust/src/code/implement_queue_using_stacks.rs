struct MyQueue {
    stack_1: Vec<i32>,
    stack_2: Vec<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {
    fn new() -> Self {
        Self {
            stack_1: Vec::new(),
            stack_2: Vec::new(),
        }
    }

    // NOTE: time complexity: O(1)
    fn push(&mut self, x: i32) {
        self.stack_1.push(x);
    }

    // NOTE: time complexity: O(n)
    fn pop(&mut self) -> i32 {
        if self.stack_2.len() == 0 {
            while let Some(x) = self.stack_1.pop() {
                self.stack_2.push(x);
            }
        }
        return self.stack_2.pop().unwrap();
    }

    // NOTE: time complexity: O(n)
    fn peek(&mut self) -> i32 {
        if self.stack_2.len() == 0 {
            while let Some(x) = self.stack_1.pop() {
                self.stack_2.push(x);
            }
        }
        return *self.stack_2.last().unwrap();
    }

    // NOTE: time complexity: O(1)
    fn empty(&self) -> bool {
        self.stack_1.len() == 0 && self.stack_2.len() == 0
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */
#[cfg(test)]
mod test {
    use super::MyQueue;

    #[test]
    fn test_my_queue_case_1() {
        let mut queue: MyQueue = MyQueue::new();
        queue.push(1);
        queue.push(2);
        assert_eq!(1, queue.peek());
        assert_eq!(1, queue.pop());
        assert_eq!(false, queue.empty());
    }
}
