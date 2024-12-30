struct Solution;

impl Solution {
    pub fn convert_to_title(mut column_number: i32) -> String {
        let mut result: Vec<char> = Vec::new();
        while column_number > 0 {
            let offset: i32 = (column_number - 1) % 26;
            result.push(('A' as u8 + offset as u8) as char);
            column_number = (column_number - 1) / 26;
        }
        result.reverse();
        result.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_convert_to_title_case_1() {
        // arrange
        let columnNumber: i32 = 1;
        let expected: String = "A".to_string();

        // act
        let actual = Solution::convert_to_title(columnNumber);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_convert_to_title_case_2() {
        // arrange
        let columnNumber: i32 = 28;
        let expected: String = "AB".to_string();

        // act
        let actual = Solution::convert_to_title(columnNumber);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_convert_to_title_case_3() {
        // arrange
        let columnNumber: i32 = 701;
        let expected: String = "ZY".to_string();

        // act
        let actual = Solution::convert_to_title(columnNumber);

        // assert
        assert_eq!(expected, actual);
    }
}
