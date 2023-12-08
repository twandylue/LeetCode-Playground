struct Solution {}

impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let n: usize = nums.len();
        let mut result: Vec<i32> = vec![0; 2 * n];
        for i in 0..nums.len() {
            result[i] = nums[i];
            result[i + n] = nums[i];
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn get_concatenation_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 1];
        let expected: Vec<i32> = vec![1, 2, 1, 1, 2, 1];

        // act
        let actual = Solution::get_concatenation(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
