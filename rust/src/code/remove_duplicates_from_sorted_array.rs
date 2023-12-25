struct Solution {}

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut l: usize = 1;
        for i in 1..nums.len() {
            if nums[i] != nums[i - 1] {
                nums[l] = nums[i];
                l += 1;
            }
        }

        l as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_duplicates_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![1, 1, 2];
        let expected: i32 = 2;

        // act
        let actual = Solution::remove_duplicates(&mut nums);

        // assert
        assert_eq!(expected, actual);
    }
}
