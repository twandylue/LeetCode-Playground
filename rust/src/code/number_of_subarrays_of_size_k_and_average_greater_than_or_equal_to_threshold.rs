struct Solution {}

impl Solution {
    pub fn num_of_subarrays(arr: Vec<i32>, k: i32, threshold: i32) -> i32 {
        let mut result: i32 = 0;
        let mut l: usize = 0;
        let mut r: usize = 0;
        let k: usize = k as usize;
        let mut accu: i32 = 0;
        while r < arr.len() {
            accu += arr[r];
            if r - l + 1 > k {
                accu -= arr[l];
                l += 1;
            }
            if r - l + 1 == k && accu as f32 / (r - l + 1) as f32 >= threshold as f32 {
                result += 1;
            }
            r += 1;
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_num_of_subarrays_case_1() {
        // arrange
        let arr: Vec<i32> = vec![2, 2, 2, 2, 5, 5, 5, 8];
        let k: i32 = 3;
        let threshold: i32 = 4;
        let expected: i32 = 3;

        // act
        let actual = Solution::num_of_subarrays(arr, k, threshold);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_of_subarrays_case_2() {
        // arrange
        let arr: Vec<i32> = vec![11, 13, 17, 23, 29, 31, 7, 5, 2, 3];
        let k: i32 = 3;
        let threshold: i32 = 5;
        let expected: i32 = 6;

        // act
        let actual = Solution::num_of_subarrays(arr, k, threshold);

        // assert
        assert_eq!(expected, actual);
    }
}
