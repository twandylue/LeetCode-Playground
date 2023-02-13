pub struct Solution {}

impl Solution {
    // TODO:
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut res = i32::MIN;
        let mut accu = 0;
        let mut left = 0;

        for r in 0..nums.len() {
            accu += nums[r];
            if accu <= 0 {
                accu -= nums[left];
                left += 1;
            }

            res = std::cmp::max(accu, res);
        }
        res
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![-2, 1, -3, 4, -1, 2, 1, -5, 4];
        let expected = 6;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let nums = vec![1];
        let expected = 1;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let nums = vec![5, 4, -1, 7, 8];
        let expected = 23;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        // TODO:
        let nums = vec![-1];
        let expected = -1;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }
}
