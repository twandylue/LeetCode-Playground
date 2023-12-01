struct Solution {}

impl Solution {
    pub fn max_turbulence_size(arr: Vec<i32>) -> i32 {
        let mut l: usize = 0;
        let mut r: usize = 1;
        let mut result: i32 = 1;
        let mut prev: &str = "";
        while l < r && r < arr.len() {
            if arr[r - 1] < arr[r] && prev != "<" {
                result = std::cmp::max(result, (r - l + 1) as i32);
                prev = "<";
                r += 1;
            } else if arr[r - 1] > arr[r] && prev != ">" {
                result = std::cmp::max(result, (r - l + 1) as i32);
                prev = ">";
                r += 1;
            } else if arr[r - 1] == arr[r] {
                l = r;
                r += 1;
                prev = "";
            } else {
                l = r - 1;
                prev = ""
            }
        }

        return result;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn max_turbulence_size_case_1() {
        // arrange
        let arr: Vec<i32> = vec![9, 4, 2, 10, 7, 8, 8, 1, 9];
        let expected: i32 = 5;

        // act
        let actual = Solution::max_turbulence_size(arr);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn max_turbulence_size_case_2() {
        // arrange
        let arr: Vec<i32> = vec![4, 8, 12, 16];
        let expected: i32 = 2;

        // act
        let actual = Solution::max_turbulence_size(arr);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn max_turbulence_size_case_3() {
        // arrange
        let arr: Vec<i32> = vec![100];
        let expected: i32 = 1;

        // act
        let actual = Solution::max_turbulence_size(arr);

        // assert
        assert_eq!(expected, actual);
    }
}
