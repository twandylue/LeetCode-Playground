pub struct Solution {}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1;

        while l <= r {
            let mid = (l + r) / 2;
            if nums[mid] == target {
                return mid as i32;
            }

            if nums[l] <= nums[mid] {
                // left part
                if nums[mid] < target || target < nums[l] {
                    l = mid + 1;
                } else {
                    r = mid - 1;
                }
            } else {
                // right part
                if nums[mid] > target || target > nums[r] {
                    r = mid - 1;
                } else {
                    l = mid + 1;
                }
            }
        }

        return -1;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_search_case_1() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let target = 0;
        let expected = 4;
        let actual = Solution::search(nums, target);

        assert_eq!(actual, expected);

        let nums2 = vec![4, 5, 6, 7, 0, 1, 2];
        let target2 = 3;
        let expected2 = -1;
        let actual2 = Solution::search(nums2, target2);

        assert_eq!(actual2, expected2);
    }
}
