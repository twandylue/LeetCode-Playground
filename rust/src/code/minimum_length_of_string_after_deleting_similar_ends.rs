struct Solution;

impl Solution {
    // NOTE: time complextiy: O(n)
    pub fn minimum_length(s: String) -> i32 {
        let s: Vec<char> = s.chars().collect();
        let mut l: usize = 0;
        let mut r: usize = s.len() - 1;
        while l < r && s[l] == s[r] {
            let tmp: char = s[l];
            while l <= r && s[l] == tmp {
                l += 1;
            }
            while l <= r && s[r] == tmp {
                r -= 1;
            }
        }
        if r < l {
            0
        } else {
            (r - l + 1) as i32
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_minimum_length_case_1() {
        // arrange
        let s: String = "ca".to_string();
        let expected: i32 = 2;

        // act
        let actual = Solution::minimum_length(s);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_minimum_length_case_2() {
        // arrange
        let s: String = "cabaabac".to_string();
        let expected: i32 = 0;

        // act
        let actual = Solution::minimum_length(s);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_minimum_length_case_3() {
        // arrange
        let s: String = "aabccabba".to_string();
        let expected: i32 = 3;

        // act
        let actual = Solution::minimum_length(s);

        // arrange
        assert_eq!(expected, actual);
    }
}
