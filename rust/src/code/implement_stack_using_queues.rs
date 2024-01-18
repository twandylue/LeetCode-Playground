use std::collections::VecDeque;

struct MyStack {
    queue: VecDeque<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyStack {
    fn new() -> Self {
        Self {
            queue: VecDeque::new(),
        }
    }

    fn push(&mut self, x: i32) {
        self.queue.push_back(x);
    }

    // NOTE: time complexity: O(n)
    fn pop(&mut self) -> i32 {
        for _ in 0..self.queue.len() - 1 {
            if let Some(n) = self.queue.pop_front() {
                self.queue.push_back(n);
            }
        }

        self.queue.pop_front().unwrap()
    }

    fn top(&self) -> i32 {
        self.queue[self.queue.len() - 1]
    }

    fn empty(&self) -> bool {
        self.queue.len() == 0
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * let obj = MyStack::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: bool = obj.empty();
 */
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_my_stack_case_1() {
        // arrange
        let mut stack = MyStack::new();

        // assert
        stack.push(1);
        stack.push(2);
        assert_eq!(stack.top(), 2);
        assert_eq!(stack.pop(), 2);
        assert_eq!(stack.empty(), false);
    }
}
