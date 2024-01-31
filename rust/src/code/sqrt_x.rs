struct Solution {}

impl Solution {
    // NOTE: time complexity: O(logn)
    // pub fn my_sqrt(x: i32) -> i32 {
    //     let x: i64 = x as i64;
    //     let mut l: i64 = 0;
    //     let mut r: i64 = (x + 1) / 2;
    //     let mut mid: i64 = 0;
    //     while l <= r {
    //         mid = (l + r) / 2;
    //         if mid.pow(2) == x {
    //             return mid as i32;
    //         } else if mid.pow(2) > x {
    //             if mid > 0 && x > (mid - 1).pow(2) {
    //                 return mid as i32 - 1;
    //             }
    //             r = mid - 1;
    //         } else {
    //             if x < (mid + 1).pow(2) {
    //                 return mid as i32;
    //             }
    //             l = mid + 1;
    //         }
    //     }
    //
    //     mid as i32
    // }

    // NOTE: time complexity: O(logn)
    pub fn my_sqrt(x: i32) -> i32 {
        let x: i64 = x as i64;
        let mut l: i64 = 0;
        let mut r: i64 = (x + 1) / 2 + 1;
        let mut result: i64 = 0;
        while l <= r {
            let mid: i64 = (l + r) / 2;
            result = mid;
            if mid.pow(2) == x {
                return mid as i32;
            } else if mid.pow(2) > x {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return if result.pow(2) > x {
            result as i32 - 1
        } else {
            result as i32
        };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_my_sqrt_case_1() {
        // arrange
        let x: i32 = 4;
        let expected: i32 = 2;

        // act
        let actual = Solution::my_sqrt(x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_my_sqrt_case_2() {
        // arrange
        let x: i32 = 8;
        let expected: i32 = 2;

        // act
        let actual = Solution::my_sqrt(x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_my_sqrt_case_3() {
        // arrange
        let x: i32 = 2147395599;
        let expected: i32 = 46339;

        // act
        let actual = Solution::my_sqrt(x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_my_sqrt_case_4() {
        // arrange
        let x: i32 = 2147483647;
        let expected: i32 = 46340;

        // act
        let actual = Solution::my_sqrt(x);

        // assert
        assert_eq!(expected, actual);
    }
}
