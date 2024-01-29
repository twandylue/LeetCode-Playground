struct Solution {}

impl Solution {
    pub fn is_perfect_square(num: i32) -> bool {
        let num: usize = num as usize;
        let mut l: usize = 0;
        let mut r: usize = num / 2 + 1;
        while l <= r {
            let mid: usize = (l + r) / 2;
            if mid.pow(2) == num {
                return true;
            }
            if mid.pow(2) > num {
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        false
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn add_is_perfect_square_case_1() {
        // arrange
        let num: i32 = 16;
        let expected: bool = true;

        // act
        let actual = Solution::is_perfect_square(num);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn add_is_perfect_square_case_2() {
        // arrange
        let num: i32 = 14;
        let expected: bool = false;

        // act
        let actual = Solution::is_perfect_square(num);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn add_is_perfect_square_case_3() {
        // arrange
        let num: i32 = 1;
        let expected: bool = true;

        // act
        let actual = Solution::is_perfect_square(num);

        // assert
        assert_eq!(expected, actual);
    }
}
