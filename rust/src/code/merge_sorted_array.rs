struct Solution {}

impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, mut m: i32, nums2: &mut Vec<i32>, mut n: i32) {
        let mut last: usize = (m + n - 1) as usize;

        while m > 0 && n > 0 && last > 0 {
            if nums1[(m - 1) as usize] > nums2[(n - 1) as usize] {
                nums1[last] = nums1[(m - 1) as usize];
                m -= 1;
            } else {
                nums1[last] = nums2[(n - 1) as usize];
                n -= 1;
            }

            last -= 1;
        }

        while n > 0 {
            nums1[last] = nums2[(n - 1) as usize];
            n -= 1;

            if last > 0 {
                last -= 1;
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn merge_sorted_array_case_1() {
        // arrange
        let mut nums1 = vec![1, 2, 3, 0, 0, 0];
        let m = 3;
        let mut nums2 = vec![2, 5, 6];
        let n = 3;
        let expected = vec![1, 2, 2, 3, 5, 6];

        // act
        Solution::merge(&mut nums1, m, &mut nums2, n);

        // assert
        assert_eq!(expected, nums1);
    }

    #[test]
    fn merge_sorted_array_case_2() {
        // arrange
        let mut nums1 = vec![1];
        let m = 1;
        let mut nums2 = vec![];
        let n = 0;
        let expected = vec![1];

        // act
        Solution::merge(&mut nums1, m, &mut nums2, n);

        // assert
        assert_eq!(expected, nums1);
    }

    #[test]
    fn merge_sorted_array_case_3() {
        // arrange
        let mut nums1 = vec![0];
        let m = 0;
        let mut nums2 = vec![1];
        let n = 1;
        let expected = vec![1];

        // act
        Solution::merge(&mut nums1, m, &mut nums2, n);

        // assert
        assert_eq!(expected, nums1);
    }
}
