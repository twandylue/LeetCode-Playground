struct Solution {}

impl Solution {
    // AAABAAAA
    // AAAA
    // 0123
    pub fn str_str(haystack: String, needle: String) -> i32 {
        if needle.len() == 0 {
            return 0;
        }

        let needle: Vec<char> = needle.chars().collect();
        let haystack: Vec<char> = haystack.chars().collect();
        let mut lps: Vec<usize> = vec![0; needle.len()];
        let mut i: usize = 1;
        let mut pre_lps: usize = 0;

        while i < needle.len() {
            if needle[pre_lps] == needle[i] {
                pre_lps += 1;
                lps[i] = pre_lps;
                i += 1;
            } else if pre_lps == 0 {
                lps[i] = 0;
                i += 1;
            } else {
                pre_lps = lps[pre_lps - 1];
            }
        }

        let mut m: usize = 0;
        let mut n: usize = 0;
        while m < haystack.len() {
            if haystack[m] == needle[n] {
                m += 1;
                n += 1;
            } else {
                if n == 0 {
                    m += 1;
                } else {
                    n = lps[n - 1];
                }
            }

            if n == needle.len() {
                return (m - n) as i32;
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_str_str_case_1() {
        // arrange
        let haystack: String = "sadbutsad".to_string();
        let needle: String = "sad".to_string();
        let expected: i32 = 0;

        // act
        let mut actual = Solution::str_str(haystack, needle);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_str_str_case_2() {
        // arrange
        let haystack: String = "leetcode".to_string();
        let needle: String = "leeto".to_string();
        let expected: i32 = -1;

        // act
        let mut actual = Solution::str_str(haystack, needle);

        // assert
        assert_eq!(expected, actual);
    }
}
