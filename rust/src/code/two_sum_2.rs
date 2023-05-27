struct Solution {}

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut s: usize = 0;
        let mut e: usize = numbers.len() - 1;
        let mut result: Vec<i32> = Vec::new();
        while s < e {
            if numbers[s] + numbers[e] > target {
                e = e - 1;
                continue;
            } else if numbers[s] + numbers[e] < target {
                s = s + 1;
            } else if numbers[s] + numbers[e] == target {
                result.push(s as i32 + 1);
                result.push(e as i32 + 1);
                return result;
            }
        }

        return result;
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
