struct Solution {}

impl Solution {
    // NOTE: time complexity: O(nlogn)
    pub fn rearrange_array(mut nums: Vec<i32>) -> Vec<i32> {
        nums.sort();
        let mut result: Vec<i32> = vec![0; nums.len()];
        let h: usize = if nums.len() % 2 == 0 {
            nums.len() / 2
        } else {
            (nums.len() + 1) / 2
        };
        let mut l: usize = 0;
        let mut r: usize = h;
        for i in 0..result.len() {
            if i % 2 == 0 && l < h {
                result[i] = nums[l];
                l += 1;
            } else if i % 2 > 0 && r < nums.len() {
                result[i] = nums[r];
                r += 1;
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_rearrange_array_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 3, 4, 5];
        let expected: Vec<i32> = vec![1, 5, 2, 4, 3];

        // act
        let actual = Solution::rearrange_array(nums);

        // assert
        assert_eq!(actual, expected);
    }
}
