struct Solution;

impl Solution {
    // time complexity: O(n)
    pub fn rotate_string(s: String, goal: String) -> bool {
        if s.len() == goal.len() && s.len() != 0 {
            let s: String = s.clone() + &s;
            if s.contains(&goal) {
                return true;
            }
        }
        false
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_rotate_string_case_1() {
        // arrange
        let s: String = "abcde".to_string();
        let goal: String = "cdeab".to_string();
        let expected: bool = true;

        // act
        let actual: bool = Solution::rotate_string(s, goal);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_rotate_string_case_2() {
        // arrange
        let s: String = "abcde".to_string();
        let goal: String = "abced".to_string();
        let expected: bool = false;

        // act
        let actual: bool = Solution::rotate_string(s, goal);

        // assert
        assert_eq!(expected, actual);
    }
}
