struct Solution;

impl Solution {
    // time complexity: O(n)
    pub fn build_array(target: Vec<i32>, n: i32) -> Vec<String> {
        let mut result: Vec<String> = Vec::new();
        let mut stack: Vec<i32> = Vec::new();
        let mut idx: usize = 0;
        for i in 1..n + 1 {
            if idx >= target.len() {
                break;
            }
            if stack == target {
                break;
            }
            if i == target[idx] {
                stack.push(i);
                result.push("Push".to_string());
                idx += 1;
            } else {
                result.push("Push".to_string());
                result.push("Pop".to_string());
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_build_array_case_1() {
        // arrange
        let target: Vec<i32> = vec![1, 3];
        let n: i32 = 3;
        let expected: Vec<String> = vec![
            "Push".to_string(),
            "Push".to_string(),
            "Pop".to_string(),
            "Push".to_string(),
        ];

        // act
        let actual = Solution::build_array(target, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_build_array_case_2() {
        // arrange
        let target: Vec<i32> = vec![1, 2, 3];
        let n: i32 = 3;
        let expected: Vec<String> =
            vec!["Push".to_string(), "Push".to_string(), "Push".to_string()];

        // act
        let actual = Solution::build_array(target, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_build_array_case_3() {
        // arrange
        let target: Vec<i32> = vec![1, 2];
        let n: i32 = 4;
        let expected: Vec<String> = vec!["Push".to_string(), "Push".to_string()];

        // act
        let actual = Solution::build_array(target, n);

        // assert
        assert_eq!(expected, actual);
    }
}
