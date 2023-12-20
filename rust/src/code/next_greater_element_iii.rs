struct Solution {}

impl Solution {
    pub fn next_greater_element(n: i32) -> i32 {
        let mut nums: Vec<i32> = n
            .to_string()
            .chars()
            .map(|x| x.to_digit(10).unwrap() as i32)
            .collect();

        for i in (0..(nums.len() - 1)).rev() {
            if nums[i] >= nums[i + 1] {
                continue;
            }

            let mut j: usize = i + 1;
            while j < nums.len() {
                if nums[j] <= nums[i] {
                    j = j - 1;
                    break;
                }
                j += 1
            }
            if j == nums.len() {
                j = nums.len() - 1;
            }

            let tmp: i32 = nums[i];
            nums[i] = nums[j];
            nums[j] = tmp;
            nums[i + 1..].sort();

            let nums_string: String = nums
                .iter()
                .map(|x| char::from_digit(*x as u32, 10).unwrap())
                .collect::<Vec<char>>()
                .iter()
                .collect::<String>();

            match nums_string.parse::<i32>() {
                Ok(n) => {
                    return n;
                }
                Err(_) => {
                    return -1;
                }
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_next_greater_element_case_1() {
        // arrange
        let n: i32 = 12;
        let expected: i32 = 21;

        // act
        let actual = Solution::next_greater_element(n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_next_greater_element_case_2() {
        // arrange
        let n: i32 = 21;
        let expected: i32 = -1;

        // act
        let actual = Solution::next_greater_element(n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_next_greater_element_case_3() {
        // arrange
        let n: i32 = 11;
        let expected: i32 = -1;

        // act
        let actual = Solution::next_greater_element(n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_next_greater_element_case_4() {
        // arrange
        let n: i32 = 2147483486;
        let expected: i32 = -1;

        // act
        let actual = Solution::next_greater_element(n);

        // assert
        assert_eq!(expected, actual);
    }
}
