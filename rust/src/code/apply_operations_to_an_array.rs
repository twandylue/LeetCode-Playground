struct Solution {}

impl Solution {
    pub fn apply_operations(mut nums: Vec<i32>) -> Vec<i32> {
        for i in 0..nums.len() - 1 {
            if nums[i] == nums[i + 1] {
                nums[i] *= 2;
                nums[i + 1] = 0;
            }
        }

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

        nums
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_apply_operations_case_1() {
        // arrange
        let nums: Vec<i32> = vec![1, 2, 2, 1, 1, 0];
        let expected: Vec<i32> = vec![1, 4, 2, 0, 0, 0];

        // act
        let actual = Solution::apply_operations(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_apply_operations_case_2() {
        // arrange
        let nums: Vec<i32> = vec![0, 1];
        let expected: Vec<i32> = vec![1, 0];

        // act
        let actual = Solution::apply_operations(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
