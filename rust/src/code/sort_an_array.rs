struct Solution {}

impl Solution {
    fn sort_array(nums: Vec<i32>) -> Vec<i32> {
        let output = Self::merge_sort_helper(nums);

        return output;
    }

    // merge sorting
    fn merge_sort_helper(nums: Vec<i32>) -> Vec<i32> {
        if nums.len() == 2 {
            if nums[0] > nums[1] {
                return vec![nums[1], nums[0]];
            } else {
                return nums;
            }
        } else if nums.len() == 1 {
            return nums;
        }

        let mid = nums.len() / 2;
        let left = Self::merge_sort_helper(nums[..mid].to_vec());
        let right = Self::merge_sort_helper(nums[mid..].to_vec());

        let sorted_array = Self::merge(left, right);

        return sorted_array;
    }

    fn merge(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut m = nums1.len();
        let mut n = nums2.len();
        let mut index = m + n - 1;
        let mut merged_vec: Vec<i32> = vec![0; m + n];

        while m > 0 && n > 0 {
            if nums1[m - 1] > nums2[n - 1] {
                merged_vec[index] = nums1[m - 1];
                m -= 1;
            } else {
                merged_vec[index] = nums2[n - 1];
                n -= 1;
            }
            if index > 0 {
                index -= 1;
            }
        }

        while m > 0 || n > 0 {
            if n > 0 {
                merged_vec[index] = nums2[n - 1];
                n -= 1;
            } else if m > 0 {
                merged_vec[index] = nums1[m - 1];
                m -= 1;
            }

            if index > 0 {
                index -= 1;
            }
        }

        return merged_vec;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
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
    fn sort_array_case_2() {
        // arrange
        let nums = vec![5, 1, 1, 2, 0, 0];
        let expected = vec![0, 0, 1, 1, 2, 5];

        // act
        let actual = Solution::sort_array(nums);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn sort_array_case_3() {
        // arrange
        let input = Vec::from([
            -74, 48, -20, 2, 10, -84, -5, -9, 11, -24, -91, 2, -71, 64, 63, 80, 28, -30, -58, -11,
            -44, -87, -22, 54, -74, -10, -55, -28, -46, 29, 10, 50, -72, 34, 26, 25, 8, 51, 13, 30,
            35, -8, 50, 65, -6, 16, -2, 21, -78, 35, -13, 14, 23, -3, 26, -90, 86, 25, -56, 91,
            -13, 92, -25, 37, 57, -20, -69, 98, 95, 45, 47, 29, 86, -28, 73, -44, -46, 65, -84,
            -96, -24, -12, 72, -68, 93, 57, 92, 52, -45, -2, 85, -63, 56, 55, 12, -85, 77, -39,
        ]);
        let expected = vec![
            -96, -91, -90, -87, -85, -84, -84, -78, -74, -74, -72, -71, -69, -68, -63, -58, -56,
            -55, -46, -46, -45, -44, -44, -39, -30, -28, -28, -25, -24, -24, -22, -20, -20, -13,
            -13, -12, -11, -10, -9, -8, -6, -5, -3, -2, -2, 2, 2, 8, 10, 10, 11, 12, 13, 14, 16,
            21, 23, 25, 25, 26, 26, 28, 29, 29, 30, 34, 35, 35, 37, 45, 47, 48, 50, 50, 51, 52, 54,
            55, 56, 57, 57, 63, 64, 65, 65, 72, 73, 77, 80, 85, 86, 86, 91, 92, 92, 93, 95, 98,
        ];

        // act
        let actual = Solution::sort_array(input);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn sort_array_case_4() {
        // arrange
        let input = Vec::from([4, 3, 2, 1]);
        let expected = vec![1, 2, 3, 4];

        // act
        let actual = Solution::sort_array(input);

        // assert
        assert_eq!(expected, actual);
    }
}
