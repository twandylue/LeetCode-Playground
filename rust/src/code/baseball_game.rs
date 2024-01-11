struct Solution {}

impl Solution {
    pub fn cal_points(operations: Vec<String>) -> i32 {
        let mut stack: Vec<String> = Vec::new();
        for i in 0..operations.len() {
            if operations[i] == "C".to_string() {
                stack.pop().unwrap();
            } else if operations[i] == "D".to_string() {
                let num: i32 = stack[stack.len() - 1].parse::<i32>().unwrap();
                stack.push((num * 2).to_string());
            } else if operations[i] == "+".to_string() {
                let num1: i32 = stack.pop().unwrap().parse::<i32>().unwrap();
                let num2: i32 = stack.pop().unwrap().parse::<i32>().unwrap();
                let total: i32 = num1 + num2;
                stack.push(num2.to_string());
                stack.push(num1.to_string());
                stack.push(total.to_string());
            } else {
                stack.push(operations[i].clone());
            }
        }

        let mut result: i32 = 0;
        for c in stack {
            result += c.parse::<i32>().unwrap();
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_cal_points_case_1() {
        // arrange
        let ops: Vec<String> = vec![
            "5".to_string(),
            "2".to_string(),
            "C".to_string(),
            "D".to_string(),
            "+".to_string(),
        ];
        let expected: i32 = 30;

        // act
        let actual = Solution::cal_points(ops);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_cal_points_case_2() {
        // arrange
        let ops: Vec<String> = vec![
            "5".to_string(),
            "-2".to_string(),
            "4".to_string(),
            "C".to_string(),
            "D".to_string(),
            "9".to_string(),
            "+".to_string(),
            "+".to_string(),
        ];
        let expected: i32 = 27;

        // act
        let actual = Solution::cal_points(ops);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_cal_points_case_3() {
        // arrange
        let ops: Vec<String> = vec!["1".to_string(), "C".to_string()];
        let expected: i32 = 0;

        // act
        let actual = Solution::cal_points(ops);

        // assert
        assert_eq!(expected, actual);
    }
}
