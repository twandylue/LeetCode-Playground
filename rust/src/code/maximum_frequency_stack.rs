use std::collections::HashMap;

struct FreqStack {
    count_map: HashMap<i32, i32>,
    group_map: HashMap<i32, Vec<i32>>,
    max_count: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl FreqStack {
    fn new() -> Self {
        Self {
            count_map: HashMap::new(),
            group_map: HashMap::new(),
            max_count: 0,
        }
    }

    fn push(&mut self, val: i32) {
        self.count_map
            .entry(val)
            .and_modify(|x| *x += 1)
            .or_insert(1);
        if let Some(&times) = self.count_map.get(&val) {
            self.max_count = std::cmp::max(self.max_count, times);
            self.group_map
                .entry(times)
                .and_modify(|x| x.push(val))
                .or_insert(vec![val]);
        }
    }

    fn pop(&mut self) -> i32 {
        if let Some(v) = self.group_map.get_mut(&self.max_count) {
            let max_count_val: i32 = v.pop().unwrap();
            if v.is_empty() {
                self.max_count -= 1;
            }
            self.count_map.entry(max_count_val).and_modify(|x| *x -= 1);
            return max_count_val;
        } else {
            unreachable!()
        }
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * let obj = FreqStack::new();
 * obj.push(val);
 * let ret_2: i32 = obj.pop();
 */

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_freq_stack_case_1() {
        // arrange
        let mut freq_stack = FreqStack::new();
        let expected1: i32 = 5;
        let expected2: i32 = 7;
        let expected3: i32 = 5;
        let expected4: i32 = 4;

        // act
        freq_stack.push(5);
        freq_stack.push(7);
        freq_stack.push(5);
        freq_stack.push(7);
        freq_stack.push(4);
        freq_stack.push(5);
        let actual1: i32 = freq_stack.pop();
        let actual2: i32 = freq_stack.pop();
        let actual3: i32 = freq_stack.pop();
        let actual4: i32 = freq_stack.pop();

        // assert
        assert_eq!(expected1, actual1);
        assert_eq!(expected2, actual2);
        assert_eq!(expected3, actual3);
        assert_eq!(expected4, actual4);
    }
}
