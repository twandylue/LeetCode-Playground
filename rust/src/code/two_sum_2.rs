struct Solution {}

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut l: usize = 0;
        let mut r: usize = numbers.len() - 1;
        while l < r {
            if numbers[l] + numbers[r] > target {
                r -= 1;
            } else if numbers[l] + numbers[r] < target {
                l += 1;
            } else if numbers[l] + numbers[r] == target {
                return Vec::from([l as i32 + 1, r as i32 + 1]);
            }
        }

        return Vec::new();
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn two_sum_2_case_1() {
        // arrange
        let numbers = vec![2, 7, 11, 15];
        let target = 9;
        let expected = vec![1, 2];

        // act
        let actual = Solution::two_sum(numbers, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn two_sum_2_case_2() {
        // arrange
        let numbers = vec![2, 3, 4];
        let target = 6;
        let expected = vec![1, 3];

        // act
        let actual = Solution::two_sum(numbers, target);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn two_sum_2_case_3() {
        // arrange
        let numbers = vec![-1, 0];
        let target = -1;
        let expected = vec![1, 2];

        // act
        let actual = Solution::two_sum(numbers, target);

        // assert
        assert_eq!(expected, actual);
    }
}
