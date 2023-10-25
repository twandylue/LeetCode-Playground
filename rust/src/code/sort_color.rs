struct Solution {}

impl Solution {
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut l: usize = 0;
        let mut m: usize = 0;
        let mut r: usize = nums.len() - 1;
        while m <= r && r > 0 {
            if nums[m] == 0 {
                let tmp = nums[m];
                nums[m] = nums[l];
                nums[l] = tmp;
                l += 1;
                m = l;
            } else if nums[m] == 2 {
                let tmp = nums[m];
                nums[m] = nums[r];
                nums[r] = tmp;
                r -= 1;
            } else {
                m += 1;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn sort_colors_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![2, 0, 2, 1, 1, 0];
        let expected: Vec<i32> = vec![0, 0, 1, 1, 2, 2];

        // act
        Solution::sort_colors(&mut nums);

        // arrange
        assert_eq!(expected, nums);
    }

    #[test]
    fn sort_colors_case_2() {
        // arrange
        let mut nums: Vec<i32> = vec![2];
        let expected: Vec<i32> = vec![2];

        // act
        Solution::sort_colors(&mut nums);

        // arrange
        assert_eq!(expected, nums);
    }
}
