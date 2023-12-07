struct Solution {}

impl Solution {
    pub fn largest_odd_number(num: String) -> String {
        let num: Vec<char> = num.chars().collect();
        for i in (0..num.len()).rev() {
            if num[i] as u8 % 2 == 0 {
                continue;
            }
            return num[0..i + 1].iter().collect::<String>();
        }
        return "".to_string();
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_largest_odd_number_case_1() {
        // arrange
        let num: String = "52".to_string();
        let expected: String = "5".to_string();

        // act
        let actual = Solution::largest_odd_number(num);

        // assert
        assert_eq!(expected, actual);
    }
}
