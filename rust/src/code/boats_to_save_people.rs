struct Solution {}

impl Solution {
    pub fn num_rescue_boats(mut people: Vec<i32>, limit: i32) -> i32 {
        people.sort();
        let mut result: i32 = 1;
        let mut l: usize = 0;
        let mut r: usize = people.len() - 1;
        while l < r {
            if people[r] == limit || people[r] + people[l] > limit {
                r -= 1;
            } else if r == l + 1 {
                break;
            } else {
                l += 1;
                r -= 1;
            }
            result += 1;
        }

        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_num_rescue_boats_case_1() {
        // arrange
        let people: Vec<i32> = vec![1, 2];
        let limit: i32 = 3;
        let expected: i32 = 1;

        // act
        let actual = Solution::num_rescue_boats(people, limit);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_rescue_boats_case_2() {
        // arrange
        let people: Vec<i32> = vec![3, 2, 2, 1];
        let limit: i32 = 3;
        let expected: i32 = 3;

        // act
        let actual = Solution::num_rescue_boats(people, limit);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_rescue_boats_case_3() {
        // arrange
        let people: Vec<i32> = vec![3, 5, 3, 4];
        let limit: i32 = 5;
        let expected: i32 = 4;

        // act
        let actual = Solution::num_rescue_boats(people, limit);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_num_rescue_boats_case_4() {
        // arrange
        let people: Vec<i32> = vec![3, 1, 7];
        let limit: i32 = 7;
        let expected: i32 = 2;

        // act
        let actual = Solution::num_rescue_boats(people, limit);

        // assert
        assert_eq!(expected, actual);
    }
}
