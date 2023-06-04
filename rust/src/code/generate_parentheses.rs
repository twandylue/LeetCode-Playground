struct Solution {}

impl Solution {
    pub fn generate_parenthesis(n: i32) -> Vec<String> {
        let mut stack: Vec<String> = Vec::new();
        let mut result: Vec<String> = Vec::new();
        Self::back_tracking(&mut stack, &mut result, n, 0, 0);

        return result;
    }

    fn back_tracking(stack: &mut Vec<String>, result: &mut Vec<String>, n: i32, open_para: i32, close_para: i32) {
        if open_para == close_para && open_para == n {
            result.push(stack[..].join(""));
            return;
        }

        if open_para < n {
            stack.push("(".to_string());
            Self::back_tracking(stack, result, n, open_para + 1, close_para);
            stack.pop().unwrap_or("".to_string());
        }

        if close_para < open_para {
            stack.push(")".to_string());
            Self::back_tracking(stack, result, n, open_para, close_para + 1);
            stack.pop().unwrap_or("".to_string());
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn generate_parenthesis_case_1() {
        // arrange
        let n = 3;
        let expected = vec!["((()))","(()())","(())()","()(())","()()()"];

        // act
        let actual = Solution::generate_parenthesis(n);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn generate_parenthesis_case_2() {
        // arrange
        let n = 1;
        let expected = vec!["()"];

        // act
        let actual = Solution::generate_parenthesis(n);

        // assert
        assert_eq!(actual, expected);
    }
}
