struct Solution {}

impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let mut left: i64 = 1;
        let mut right: i64 = *piles.iter().max().unwrap() as i64;

        while left <= right {
            let mid: i64 = (left + right) / 2;
            let mut count: i64 = 0;
            for pile in &piles {
                // NOTE: https://stackoverflow.com/questions/2422712/rounding-integer-division-instead-of-truncating
                count += (*pile as i64 + mid - 1) / mid;
            }

            if count <= h as i64 {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        left as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn min_eating_speed_case_1() {
        // arrange
        let piles = vec![3, 6, 7, 11];
        let h = 8;
        let expected = 4;

        // act
        let actual = Solution::min_eating_speed(piles, h);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn min_eating_speed_case_2() {
        // arrange
        let piles = vec![30, 11, 23, 4, 20];
        let h = 5;
        let expected = 30;

        // act
        let actual = Solution::min_eating_speed(piles, h);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn min_eating_speed_case_3() {
        // arrange
        let piles = vec![30, 11, 23, 4, 20];
        let h = 6;
        let expected = 23;

        // act
        let actual = Solution::min_eating_speed(piles, h);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn min_eating_speed_case_4() {
        // arrange
        let piles = vec![805306368, 805306368, 805306368];
        let h = 1000000000;
        let expected = 3;

        // act
        let actual = Solution::min_eating_speed(piles, h);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn min_eating_speed_case_5() {
        // arrange
        let piles = vec![1, 1, 1, 999999999];
        let h = 10;
        let expected = 142857143;

        // act
        let actual = Solution::min_eating_speed(piles, h);

        // assert
        assert_eq!(expected, actual);
    }
}
