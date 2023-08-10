pub struct Solution {}

impl Solution {
    // NOTE: time complexity O(n), space complexity O(1)
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let mut goal = nums.len() - 1;
        for i in (0..nums.len()).rev() {
            if i + nums[i] as usize >= goal {
                goal = i;
            }
        }

        return if goal > 0 { false } else { true };
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![2, 3, 1, 1, 4];
        let expected = true;
        let actual = Solution::can_jump(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let nums = vec![3, 2, 1, 0, 4];
        let expected = false;
        let actual = Solution::can_jump(nums);

        assert_eq!(expected, actual);
    }
}
