struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn sorted_squares(nums: Vec<i32>) -> Vec<i32> {
        let mut result: Vec<i32> = vec![0; nums.len()];
        let mut l: usize = 0;
        let mut r: usize = nums.len() - 1;
        let mut i: usize = nums.len() - 1;
        while l <= r && i >= 0 {
            if nums[l].pow(2) >= nums[r].pow(2) {
                result[i] = nums[l].pow(2);
                l += 1;
            } else {
                result[i] = nums[r].pow(2);
                if r.checked_sub(1).is_none() {
                    break;
                }
                r -= 1;
            }
            if i.checked_sub(1).is_none() {
                break;
            }
            i -= 1;
        }
        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_sorted_squares_case_1() {
        // arrange
        let nums: Vec<i32> = vec![-4, -1, 0, 3, 10];
        let expected: Vec<i32> = vec![0, 1, 9, 16, 100];

        // act
        let actual = Solution::sorted_squares(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_sorted_squares_case_2() {
        // arrange
        let nums: Vec<i32> = vec![-7, -3, 2, 3, 11];
        let expected: Vec<i32> = vec![4, 9, 9, 49, 121];

        // act
        let actual = Solution::sorted_squares(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
