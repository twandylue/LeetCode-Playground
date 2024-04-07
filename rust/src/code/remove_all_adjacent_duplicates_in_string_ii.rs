struct Solution {}

impl Solution {
    // NOTE: tmie complexity: O(n)
    pub fn remove_duplicates(s: String, k: i32) -> String {
        let mut stack: Vec<(char, i32)> = Vec::new();
        let s: Vec<char> = s.chars().collect();
        for i in 0..s.len() {
            let mut count: i32 = 1;
            if stack.len() > 0 && stack[stack.len() - 1].0 == s[i] {
                count += stack[stack.len() - 1].1;
            }
            if count == k {
                while stack.len() > 0 && stack[stack.len() - 1].0 == s[i] {
                    stack.pop().unwrap();
                    count -= 1;
                }
            } else {
                stack.push((s[i], count));
            }
        }

        stack.iter().map(|x| x.0).collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_remove_duplicates_case_1() {
        // arrange
        let s: String = "abcd".to_string();
        let k: i32 = 2;
        let expected: String = "abcd".to_string();

        // act
        let actual = Solution::remove_duplicates(s, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_remove_duplicates_case_2() {
        // arrange
        let s: String = "deeedbbcccbdaa".to_string();
        let k: i32 = 3;
        let expected: String = "aa".to_string();

        // act
        let actual = Solution::remove_duplicates(s, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_remove_duplicates_case_3() {
        // arrange
        let s: String = "pbbcggttciiippooaais".to_string();
        let k: i32 = 2;
        let expected: String = "ps".to_string();

        // act
        let actual = Solution::remove_duplicates(s, k);

        // assert
        assert_eq!(expected, actual);
    }
}
