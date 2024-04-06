struct Solution {}

impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut stack: Vec<char> = Vec::new();
        for i in 0..s.len() {
            if let Some(&c) = stack.iter().last() {
                if c == s[i] {
                    stack.pop();
                } else {
                    stack.push(s[i]);
                }
                continue;
            }
            stack.push(s[i]);
        }

        stack.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn remove_duplicates_case_1() {
        // arrange
        let s: String = "abbaca".to_string();
        let expected: String = "ca".to_string();

        // act
        let actual = Solution::remove_duplicates(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn remove_duplicates_case_2() {
        // arrange
        let s: String = "azxxzy".to_string();
        let expected: String = "ay".to_string();

        // act
        let actual = Solution::remove_duplicates(s);

        // assert
        assert_eq!(expected, actual);
    }
}
