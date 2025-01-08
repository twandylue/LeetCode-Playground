struct Solution;

impl Solution {
    // time complexity: O(n), space complexity: O(1)
    pub fn rotate(nums: &mut Vec<i32>, k: i32) {
        let k: usize = k as usize % nums.len();
        if k == 0 {
            return;
        }
        // Reverse the whole array
        Self::reverse(nums, 0, nums.len() - 1);
        // Reverse the first k elemetns
        Self::reverse(nums, 0, k - 1);
        // Reverse the rest of the array
        Self::reverse(nums, k, nums.len() - 1);
    }

    fn reverse(nums: &mut Vec<i32>, mut l: usize, mut r: usize) {
        while l <= r {
            let tmp: i32 = nums[l];
            nums[l] = nums[r];
            nums[r] = tmp;
            l += 1;
            if r.checked_sub(1).is_some() {
                r -= 1;
            }
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_rotate_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7];
        let k: i32 = 3;
        let expected: Vec<i32> = vec![5, 6, 7, 1, 2, 3, 4];

        // act
        Solution::rotate(&mut nums, k);

        // assert
        assert_eq!(expected, nums);
    }

    #[test]
    fn test_rotate_case_2() {
        // arrange
        let mut nums: Vec<i32> = vec![1, 2];
        let k: i32 = 3;
        let expected: Vec<i32> = vec![2, 1];

        // act
        Solution::rotate(&mut nums, k);

        // assert
        assert_eq!(expected, nums);
    }

    #[test]
    fn test_rotate_case_3() {
        // arrange
        let mut nums: Vec<i32> = vec![1];
        let k: i32 = 0;
        let expected: Vec<i32> = vec![1];

        // act
        Solution::rotate(&mut nums, k);

        // assert
        assert_eq!(expected, nums);
    }
}
