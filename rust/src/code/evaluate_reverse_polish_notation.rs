struct Solution {}

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        if tokens.len() < 3 {
            return tokens[0].parse::<i32>().unwrap();
        }

        let mut stack: Vec<i32> = Vec::new();

        for t in tokens.clone() {
            match t.as_str() {
                "+" => {
                    let arg_1 = stack.pop().unwrap();
                    let arg_2 = stack.pop().unwrap();
                    stack.push(arg_2 + arg_1);
                }
                "-" => {
                    let arg_1 = stack.pop().unwrap();
                    let arg_2 = stack.pop().unwrap();
                    stack.push(arg_2 - arg_1);
                }
                "*" => {
                    let arg_1 = stack.pop().unwrap();
                    let arg_2 = stack.pop().unwrap();
                    stack.push(arg_2 * arg_1);
                }
                "/" => {
                    let arg_1 = stack.pop().unwrap();
                    let arg_2 = stack.pop().unwrap();
                    stack.push(arg_2 / arg_1);
                }
                _ => {
                    stack.push(t.parse::<i32>().unwrap());
                }
            }
        }

        return *stack.last().unwrap();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn eval_rpn_case_1() {
        // arrange
        let tokens = vec![
            "2".to_string(),
            "1".to_string(),
            "+".to_string(),
            "3".to_string(),
            "*".to_string(),
        ];
        let expected = 9;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn eval_rpn_case_2() {
        // arrange
        let tokens = vec![
            "4".to_string(),
            "13".to_string(),
            "5".to_string(),
            "/".to_string(),
            "+".to_string(),
        ];
        let expected = 6;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn eval_rpn_case_3() {
        // arrange
        let tokens = vec![
            "10".to_string(),
            "6".to_string(),
            "9".to_string(),
            "3".to_string(),
            "+".to_string(),
            "-11".to_string(),
            "*".to_string(),
            "/".to_string(),
            "*".to_string(),
            "17".to_string(),
            "+".to_string(),
            "5".to_string(),
            "+".to_string(),
        ];
        let expected = 22;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn eval_rpn_case_4() {
        // arrange
        let tokens = vec!["18".to_string()];
        let expected = 18;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn eval_rpn_case_5() {
        // arrange
        let tokens = vec!["4".to_string(), "3".to_string(), "-".to_string()];
        let expected = 1;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn eval_rpn_case_6() {
        // arrange
        let tokens = vec![
            "3".to_string(),
            "11".to_string(),
            "+".to_string(),
            "5".to_string(),
            "-".to_string(),
        ];
        let expected = 9;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn eval_rpn_case_7() {
        // arrange
        let tokens = vec![
            "3".to_string(),
            "11".to_string(),
            "5".to_string(),
            "+".to_string(),
            "-".to_string(),
        ];
        let expected = -13;

        // act
        let actual = Solution::eval_rpn(tokens);

        // assert
        assert_eq!(expected, actual);
    }
}
