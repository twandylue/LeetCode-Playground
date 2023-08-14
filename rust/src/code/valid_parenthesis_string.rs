struct Solution {}

impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let s: Vec<char> = s.chars().collect();
        let mut left_min = 0;
        let mut left_max = 0;

        for c in s {
            if c == '(' {
                left_max += 1;
                left_min += 1;
            } else if c == ')' {
                left_max -= 1;
                left_min -= 1;
            } else if c == '*' {
                left_max += 1;
                left_min -= 1;
            }

            if left_max < 0 {
                return false;
            }

            if left_min < 0 {
                left_min = 0;
            }
        }

        return left_min == 0;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_chech_valid_string_case_1() {
        // arrange
        let s = String::from("()");
        let expected = true;

        // act
        let actual = Solution::check_valid_string(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_chech_valid_string_case_2() {
        // arrange
        let s = String::from("(*)");
        let expected = true;

        // act
        let actual = Solution::check_valid_string(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_chech_valid_string_case_3() {
        // arrange
        let s = String::from("(*))");
        let expected = true;

        // act
        let actual = Solution::check_valid_string(s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_chech_valid_string_case_4() {
        // arrange
        let s = String::from("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())");
        let expected = false;

        // act
        let actual = Solution::check_valid_string(s);

        // assert
        assert_eq!(actual, expected);
    }
}
