pub struct Solution {}

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let mut l = 0;
        let mut r = nums.len() - 1;

        while l < r {
            let mid = (l + r) / 2;
            if nums[mid] == target {
                return mid as i32;
            }

            // TODO:
        }

        return 0;
    }

    pub fn tests() {
        let nums = vec![4, 5, 6, 7, 0, 1, 2];
        let target = 0;
        let expected = 4;

        let nums2 = vec![4, 5, 6, 7, 0, 1, 2];
        let target2 = 3;
        let expected2 = -1;
    }
}
