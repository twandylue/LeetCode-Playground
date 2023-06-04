struct MinStack {
    stack: Vec<i32>,
    min_stack: Vec<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {
    fn new() -> Self {
        Self {
            stack: Vec::<i32>::new(),
            min_stack: Vec::<i32>::new(),
        }
    }

    fn push(&mut self, val: i32) {
        self.stack.push(val);

        if self.min_stack.is_empty() {
            self.min_stack.push(val);
        } else if val <= *self.min_stack.last().unwrap() {
            self.min_stack.push(val);
        } else {
            self.min_stack.push(*self.min_stack.last().unwrap());
        }
    }

    fn pop(&mut self) {
        self.stack.pop().unwrap();
        self.min_stack.pop().unwrap();
    }

    fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }

    fn get_min(&self) -> i32 {
        *self.min_stack.last().unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn min_stack_case_1() {
        // arrange
        let expected1 = -3;
        let expected2 = 0;
        let expected3 = -2;
        let mut obj = MinStack::new();

        // act
        obj.push(-2);
        obj.push(0);
        obj.push(-3);
        let actual1 = obj.get_min();
        obj.pop();
        let actual2: i32 = obj.top();
        let actual3: i32 = obj.get_min();

        // assert
        assert_eq!(expected1, actual1);
        assert_eq!(expected2, actual2);
        assert_eq!(expected3, actual3);
    }

    #[test]
    fn min_stack_case_2() {
        // arrange
        let expected1 = -2;
        let expected2 = -1;
        let expected3 = -2;
        let mut obj = MinStack::new();

        // act
        obj.push(-2);
        obj.push(0);
        obj.push(-1);
        let actual1 = obj.get_min();
        let actual2: i32 = obj.top();
        obj.pop();
        let actual3: i32 = obj.get_min();

        // assert
        assert_eq!(expected1, actual1);
        assert_eq!(expected2, actual2);
        assert_eq!(expected3, actual3);
    }
}
