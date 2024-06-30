struct Solution {}

impl Solution {
    pub fn min_flips(s: String) -> i32 {
        let mut result: i32 = i32::MAX;
        let n: usize = s.len();
        let s: Vec<char> = s.chars().collect();
        let new_s: Vec<char> = [&s[..], &s[..]].concat();
        // let new_s: Vec<char> = s.clone().into_iter().chain(s.into_iter()).collect();

        let mut target_1: Vec<char> = Vec::new();
        let mut target_2: Vec<char> = Vec::new();
        for i in 0..new_s.len() {
            if i % 2 == 0 {
                target_1.push('0');
                target_2.push('1');
            } else {
                target_1.push('1');
                target_2.push('0');
            }
        }

        let mut diff_1: i32 = 0;
        let mut diff_2: i32 = 0;
        let mut l: usize = 0;
        for r in 0..new_s.len() {
            if new_s[r] != target_1[r] {
                diff_1 += 1;
            }
            if new_s[r] != target_2[r] {
                diff_2 += 1;
            }
            if r - l + 1 > n {
                if new_s[l] != target_1[l] {
                    diff_1 -= 1;
                }
                if new_s[l] != target_2[l] {
                    diff_2 -= 1;
                }
                l += 1;
            }
            if r - l + 1 == n {
                result = std::cmp::min(result, std::cmp::min(diff_1, diff_2));
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_min_flips_case_1() {
        // arrange
        let s: String = "111000".to_string();
        let expected: i32 = 2;

        // act
        let actual = Solution::min_flips(s);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_flips_case_2() {
        // arrange
        let s: String = "010".to_string();
        let expected: i32 = 0;

        // act
        let actual = Solution::min_flips(s);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_flips_case_3() {
        // arrange
        let s: String = "1110".to_string();
        let expected: i32 = 1;

        // act
        let actual = Solution::min_flips(s);

        // arrange
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_min_flips_case_4() {
        // arrange
        let s: String = "01001001101".to_string();
        let expected: i32 = 2;

        // act
        let actual = Solution::min_flips(s);

        // arrange
        assert_eq!(expected, actual);
    }
}
