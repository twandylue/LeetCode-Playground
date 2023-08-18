use std::collections::HashSet;

struct Solution {}

impl Solution {
    pub fn is_happy(mut n: i32) -> bool {
        let mut set: HashSet<i32> = HashSet::new();
        while !set.contains(&n) {
            if n == 1 {
                return true;
            }

            set.insert(n);
            n = Self::sum_of_squares(n);
        }

        false
    }

    fn sum_of_squares(mut n: i32) -> i32 {
        let mut output = 0;
        while n > 0 {
            let digit = n % 10;
            output += digit.pow(2);
            n = n / 10;
        }

        output
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_is_happy_case_1() {
        // arrange
        let n = 19;
        let expected = true;

        // act
        let actual = Solution::is_happy(n);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_is_happy_case_2() {
        // arrange
        let n = 2;
        let expected = false;

        // act
        let actual = Solution::is_happy(n);

        // assert
        assert_eq!(actual, expected);
    }
}
