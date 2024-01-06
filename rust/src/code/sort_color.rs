struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    // This is DNF problem (The Dutch national flag).
    pub fn sort_colors(nums: &mut Vec<i32>) {
        let mut l: usize = 0;
        let mut i: usize = 0;
        let mut r: usize = nums.len() - 1;
        while i <= r {
            if nums[i] == 0 {
                nums.swap(i, l);
                l += 1;
                i += 1;
            } else if nums[i] == 2 {
                nums.swap(i, r);
                if r.checked_sub(1).is_none() {
                    break;
                }
                r -= 1;
            } else {
                i += 1;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sort_colors_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![2, 0, 2, 1, 1, 0];
        let expected: Vec<i32> = vec![0, 0, 1, 1, 2, 2];

        // act
        Solution::sort_colors(&mut nums);

        // arrange
        assert_eq!(expected, nums);
    }

    #[test]
    fn test_sort_colors_case_2() {
        // arrange
        let mut nums: Vec<i32> = vec![2];
        let expected: Vec<i32> = vec![2];

        // act
        Solution::sort_colors(&mut nums);

        // arrange
        assert_eq!(expected, nums);
    }

    #[test]
    fn test_sort_colors_case_3() {
        // arrange
        let mut nums: Vec<i32> = vec![2, 2];
        let expected: Vec<i32> = vec![2, 2];

        // act
        Solution::sort_colors(&mut nums);

        // arrange
        assert_eq!(expected, nums);
    }
}
