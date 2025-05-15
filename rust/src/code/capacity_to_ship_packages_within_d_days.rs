struct Solution {}

impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
        let mut l: i32 = weights.iter().fold(0, |acc, x| acc + x) / days;
        let mut r: i32 = weights.iter().fold(0, |acc, x| acc + x);
        let mut result: i32 = r;
        while l <= r {
            let mid: i32 = (l + r) / 2;
            if Self::can_ship(mid, &weights, days) {
                if mid.checked_sub(1).is_none() {
                    break;
                }
                result = std::cmp::min(result, mid);
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        result
    }

    fn can_ship(cap: i32, weights: &Vec<i32>, days: i32) -> bool {
        let mut accu: i32 = 0;
        let mut count: i32 = 0;
        for w in weights.iter() {
            if cap < *w {
                return false;
            }
            accu += *w;
            if accu > cap {
                count += 1;
                accu = *w;
            }
        }

        if accu > 0 {
            count += 1;
        }

        count <= days
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_ship_within_days_case_1() {
        // arrange
        let weights: Vec<i32> = vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
        let days: i32 = 5;
        let expected: i32 = 15;

        // act
        let actual = Solution::ship_within_days(weights, days);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_ship_within_days_case_2() {
        // arrange
        let weights: Vec<i32> = vec![3, 2, 2, 4, 1, 4];
        let days: i32 = 3;
        let expected: i32 = 6;

        // act
        let actual = Solution::ship_within_days(weights, days);

        // assert
        assert_eq!(expected, actual);
    }
}
