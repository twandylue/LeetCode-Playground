struct Solution {}

impl Solution {
    // NOTE: time complexity: O(2n)
    pub fn longest_prefix(s: String) -> String {
        let s: Vec<char> = s.chars().collect();
        let mut prev_lps: usize = 0;
        let mut i: usize = 1;
        let mut lps: Vec<usize> = vec![0; s.len()];
        while i < s.len() {
            if s[prev_lps] == s[i] {
                prev_lps += 1;
                lps[i] = prev_lps;
                i += 1;
            } else if prev_lps == 0 {
                lps[i] = 0;
                i += 1;
            } else {
                prev_lps = lps[prev_lps - 1];
            }
        }

        match lps.last() {
            Some(&n) => {
                if n == 0 {
                    "".to_string()
                } else {
                    s[..n].iter().collect::<String>()
                }
            }
            _ => unreachable!("Get away."),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn longest_prefix_case_1() {
        // arrange
        let s = "level".to_string();
        let expected = "l".to_string();

        // act
        let actual = Solution::longest_prefix(s);

        // assert
        assert_eq!(expected, actual);
        assert_eq!(
            Solution::longest_prefix("ababab".to_string()),
            "abab".to_string()
        );
        assert_eq!(
            Solution::longest_prefix("leetcodeleet".to_string()),
            "leet".to_string()
        );
        assert_eq!(Solution::longest_prefix("a".to_string()), "".to_string());
    }

    #[test]
    fn longest_prefix_case_2() {
        // arrange
        let s = "ababab".to_string();
        let expected = "abab".to_string();

        // act
        let actual = Solution::longest_prefix(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn longest_prefix_case_3() {
        // arrange
        let s = "aabaaa".to_string();
        let expected = "aa".to_string();

        // act
        let actual = Solution::longest_prefix(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn longest_prefix_case_4() {
        // arrange
        let s = "acccbaaacccbaac".to_string();
        let expected = "ac".to_string();

        // act
        let actual = Solution::longest_prefix(s);

        // assert
        assert_eq!(expected, actual);
    }
}
