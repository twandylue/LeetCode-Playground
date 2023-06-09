struct Solution {}

impl Solution {
    fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        let mut output = nums.clone();
        Self::quick_sort_helper(0, nums.len() - 1, &mut output);

        return output;
    }

    fn quick_sort_helper(l: usize, r: usize, nums: &mut Vec<i32>) {
        todo!();
        // if l < r && r < nums.len() {
        //     let pivot = r;
        //     if pivot == 0 {
        //         return;
        //     }

        //     Self::partition(l, r - 1, pivot, nums);
        //     Self::quick_sort_helper(l, pivot - 1, nums);
        //     Self::quick_sort_helper(pivot + 1, r, nums);
        // }
    }

    fn partition(mut l: usize, mut r: usize, pivot: usize, nums: &mut Vec<i32>) {
        while l < r && r < nums.len() && r > 0 {
            if nums[l] <= nums[pivot] {
                l += 1;
            } else if nums[l] > nums[pivot] && nums[r] > nums[pivot] {
                r -= 1;
            } else if nums[l] > nums[pivot] && nums[r] <= nums[pivot] {
                Self::swap(l, r, nums);
                l += 1;
                r -= 1;
            }
        }

        if nums[l] > nums[pivot] {
            Self::swap(pivot, l, nums);
        }
    }

    fn swap(l: usize, r: usize, nums: &mut Vec<i32>) {
        let temp = nums[l];
        nums[l] = nums[r];
        nums[r] = temp;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[ignore]
    fn sort_array_case_1() {
        // arrange
        let nums = vec![5, 2, 3, 1];
        let expected = vec![1, 2, 3, 5];

        // act
        let actual = Solution::sort_array(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    #[ignore]
    fn sort_array_case_2() {
        // arrange
        let nums = vec![5, 1, 1, 2, 0, 0];
        let expected = vec![0, 0, 1, 1, 2, 5];

        // act
        let actual = Solution::sort_array(nums);

        // assert
        assert_eq!(expected, actual);
    }
}
