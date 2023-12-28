struct Solution {}

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let mut l: usize = 0;
        for r in 0..nums.len() {
            if nums[r] == 0 {
                continue;
            }
            nums[l] = nums[r];
            l += 1;
        }

        for i in l..nums.len() {
            nums[i] = 0;
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_move_zeroes_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![0, 1, 0, 3, 12];
        let expected: Vec<i32> = vec![1, 3, 12, 0, 0];

        // act
        Solution::move_zeroes(&mut nums);

        // assert
        assert_eq!(expected, nums);
    }
}
