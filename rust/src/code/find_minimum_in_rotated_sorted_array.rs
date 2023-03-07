use std::cmp;

pub struct Solution {}

impl Solution {
    pub fn find_min(nums: Vec<i32>) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1;
        let mut ret = nums[0];

        while l <= r {
            if nums[l] < nums[r] {
                ret = cmp::min(ret, nums[l]);
                break;
            }

            let mid = (l + r) / 2;
            ret = cmp::min(nums[mid], ret);

            if nums[l] <= nums[mid] {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return ret;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let nums = vec![3, 4, 5, 1, 2];
        let expected = 1;
        let actual = Solution::find_min(nums);

        assert_eq!(actual, expected);

        let nums2 = vec![4, 5, 6, 7, 0, 1, 2];
        let expected2 = 0;
        let actual2 = Solution::find_min(nums2);

        assert_eq!(actual2, expected2);

        let nums3 = vec![11, 13, 15, 17];
        let expected3 = 11;
        let actual3 = Solution::find_min(nums3);

        assert_eq!(actual3, expected3);
    }
}
