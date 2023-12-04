struct Solution {}

impl Solution {
    pub fn replace_elements(arr: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![0; arr.len() + 1];
        result[arr.len()] = -1;
        for i in (0..arr.len()).rev() {
            result[i] = std::cmp::max(result[i + 1], arr[i]);
        }

        result[1..].to_vec()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn replace_elements_case_1() {
        // arrange
        let arr: Vec<i32> = vec![17, 18, 5, 4, 6, 1];
        let expected: Vec<i32> = vec![18, 6, 6, 6, 1, -1];

        // act
        let actual = Solution::replace_elements(arr);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn replace_elements_case_2() {
        // arrange
        let arr: Vec<i32> = vec![400];
        let expected: Vec<i32> = vec![-1];

        // act
        let actual = Solution::replace_elements(arr);

        // assert
        assert_eq!(expected, actual);
    }
}
