struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn sort_array_by_parity(mut nums: Vec<i32>) -> Vec<i32> {
        let mut l: usize = 0;
        let mut r: usize = 0;
        while l < nums.len() && r < nums.len() {
            if nums[r] % 2 == 0 {
                let tmp: i32 = nums[l];
                nums[l] = nums[r];
                nums[r] = tmp;
                l += 1;
            }
            r += 1;
        }
        nums
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sort_array_by_parity_case_1() {
        // arrange
        let nums: Vec<i32> = vec![3, 1, 2, 4];
        let expected: Vec<i32> = vec![2, 4, 3, 1];

        // act
        let actual: Vec<i32> = Solution::sort_array_by_parity(nums);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_sort_array_by_parity_case_2() {
        // arrange
        let nums: Vec<i32> = vec![0];
        let expected: Vec<i32> = vec![0];

        // act
        let actual: Vec<i32> = Solution::sort_array_by_parity(nums);

        // arrange
        assert_eq!(expected, actual);
    }
}
