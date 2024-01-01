struct Solution {}

impl Solution {
    pub fn remove_element(nums: &mut Vec<i32>, val: i32) -> i32 {
        let mut k: usize = 0;
        for i in 0..nums.len() {
            if nums[i] != val {
                nums[k] = nums[i];
                k += 1;
            }
        }

        k as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_element_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![3, 2, 2, 3];
        let val: i32 = 3;
        let expected: i32 = 2;

        // act
        let actual = Solution::remove_element(&mut nums, val);

        // assert
        assert_eq!(expected, actual);
    }
}
