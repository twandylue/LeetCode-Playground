struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn wiggle_sort(nums: &mut Vec<i32>) {
        nums.sort();
        let mut result: Vec<i32> = Vec::new();
        let mut l: usize = if nums.len() % 2 == 0 {
            nums.len() / 2 - 1
        } else {
            nums.len() / 2
        };
        let h: usize = l;
        let mut r: usize = nums.len() - 1;

        while result.len() != nums.len() {
            result.push(nums[l]);
            if l > 0 {
                l -= 1;
            }
            if r > h {
                result.push(nums[r]);
                r -= 1;
            }
        }

        for i in 0..result.len() {
            nums[i] = result[i];
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_wiggle_sort_case_1() {
        // arrange
        let mut nums: Vec<i32> = vec![1, 5, 1, 1, 6, 4];
        let expected: Vec<i32> = vec![1, 6, 1, 5, 1, 4];

        // act
        Solution::wiggle_sort(&mut nums);

        // assert
        assert_eq!(expected, nums);
    }

    #[test]
    fn add_two_numbers_case_2() {
        // arrange
        let mut nums: Vec<i32> = vec![1, 3, 2, 2, 3, 1];
        let expected: Vec<i32> = vec![2, 3, 1, 3, 1, 2];

        // act
        Solution::wiggle_sort(&mut nums);

        // assert
        assert_eq!(expected, nums);
    }
}
