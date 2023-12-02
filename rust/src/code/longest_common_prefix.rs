struct Solution {}

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        let mut result: Vec<char> = Vec::new();
        for i in 0..strs[0].len() {
            for s in strs.iter() {
                if i == s.len() || strs[0].chars().nth(i).unwrap() != s.chars().nth(i).unwrap() {
                    return result.into_iter().collect::<String>();
                }
            }
            result.push(strs[0].chars().nth(i).unwrap());
        }

        result.into_iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn longest_common_prefix_case_1() {
        // arrange
        let strs: Vec<String> = vec![
            "flower".to_string(),
            "flow".to_string(),
            "flight".to_string(),
        ];
        let expected: String = "fl".to_string();

        // act
        let actual = Solution::longest_common_prefix(strs);

        // assert
        assert_eq!(expected, actual)
    }
}
