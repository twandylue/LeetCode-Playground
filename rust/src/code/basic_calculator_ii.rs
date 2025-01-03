struct Solution;

impl Solution {
    pub fn calculate(s: String) -> i32 {
        // time complexity: O(n)
        let mut curr: u32 = 0;
        let mut stack: Vec<i32> = Vec::new();
        let mut last_operator: char = '+';
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            if s[i].is_digit(10) {
                curr = curr * 10 + s[i].to_digit(10).unwrap();
            }
            if s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/' || i == s.len() - 1 {
                if last_operator == '+' {
                    stack.push(curr as i32);
                } else if last_operator == '-' {
                    stack.push(-1 * (curr as i32));
                } else if last_operator == '*' {
                    if let Some(num) = stack.pop() {
                        stack.push(num * (curr as i32));
                    }
                } else {
                    if let Some(num) = stack.pop() {
                        stack.push(num / (curr as i32));
                    }
                }
                last_operator = s[i];
                curr = 0;
            }
        }
        stack.iter().sum()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_calculate_case_1() {
        // arrange
        let s: String = "3+2*2".to_string();
        let expected: i32 = 7;

        // act
        let actual = Solution::calculate(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_calculate_case_2() {
        // arrange
        let s: String = " 3/2 ".to_string();
        let expected: i32 = 1;

        // act
        let actual = Solution::calculate(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_calculate_case_3() {
        // arrange
        let s: String = " 3+5 / 2 ".to_string();
        let expected: i32 = 5;

        // act
        let actual = Solution::calculate(s);

        // assert
        assert_eq!(expected, actual);
    }
}
