struct Solution;

impl Solution {
    // time complexity: O(n)
    pub fn single_number(nums: Vec<i32>) -> i32 {
        let mut result: i32 = 0;
        for num in nums {
            result ^= num;
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_single_number_case_1() {
        // arrange
        let nums: Vec<i32> = vec![2, 2, 1];
        let expected: i32 = 1;

        // act
        let actual = Solution::single_number(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_single_number_case_2() {
        // arrange
        let nums: Vec<i32> = vec![4, 1, 2, 1, 2];
        let expected: i32 = 4;

        // act
        let actual = Solution::single_number(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_single_number_case_3() {
        // arrange
        let nums: Vec<i32> = vec![1];
        let expected: i32 = 1;

        // act
        let actual = Solution::single_number(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
