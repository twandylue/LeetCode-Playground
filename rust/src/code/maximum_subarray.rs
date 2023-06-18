pub struct Solution {}

impl Solution {
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut res = i32::MIN;
        let mut accu = 0;

        for r in 0..nums.len() {
            accu += nums[r];
            res = std::cmp::max(accu, res);
            if accu <= 0 {
                accu = 0;
            }
        }
        res
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn max_sub_array_case_1() {
        let nums = vec![-2, 1, -3, 4, -1, 2, 1, -5, 4];
        let expected = 6;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn max_sub_array_case_2() {
        let nums = vec![1];
        let expected = 1;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn max_sub_array_case_3() {
        let nums = vec![5, 4, -1, 7, 8];
        let expected = 23;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn max_sub_array_case_4() {
        let nums = vec![-1];
        let expected = -1;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn max_sub_array_case_5() {
        let nums = vec![1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4];
        let expected = 6;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }

    #[test]
    fn max_sub_array_case_6() {
        let nums = vec![-2, -1];
        let expected = -1;
        let actual = Solution::max_sub_array(nums);

        assert_eq!(expected, actual);
    }
}
