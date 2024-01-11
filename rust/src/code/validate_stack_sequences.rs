struct Solution {}

impl Solution {
    pub fn validate_stack_sequences(pushed: Vec<i32>, popped: Vec<i32>) -> bool {
        let mut stack: Vec<i32> = Vec::new();
        let mut p: usize = 0;
        for i in 0..pushed.len() {
            stack.push(pushed[i]);
            while p < popped.len() && stack.len() > 0 && popped[p] == stack[stack.len() - 1] {
                stack.pop().unwrap();
                p += 1;
            }
        }

        stack.len() == 0
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_validate_stack_sequences_case_1() {
        // arrange
        let pushed: Vec<i32> = vec![1, 2, 3, 4, 5];
        let popped: Vec<i32> = vec![4, 5, 3, 2, 1];
        let expected: bool = true;

        // act
        let actual = Solution::validate_stack_sequences(pushed, popped);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_validate_stack_sequences_case_2() {
        // arrange
        let pushed: Vec<i32> = vec![1, 2, 3, 4, 5];
        let popped: Vec<i32> = vec![4, 3, 5, 1, 2];
        let expected: bool = false;

        // act
        let actual = Solution::validate_stack_sequences(pushed, popped);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_validate_stack_sequences_case_3() {
        // arrange
        let pushed: Vec<i32> = vec![1, 0];
        let popped: Vec<i32> = vec![1, 0];
        let expected: bool = true;

        // act
        let actual = Solution::validate_stack_sequences(pushed, popped);

        // assert
        assert_eq!(expected, actual);
    }
}
