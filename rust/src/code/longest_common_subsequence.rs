pub struct Solution {}

impl Solution {
    pub fn longest_common_subsequence(text1: String, text2: String) -> i32 {
        let n = text1.len();
        let m = text2.len();
        let c1 = text1.chars().collect::<Vec<char>>();
        let c2 = text2.chars().collect::<Vec<char>>();
        let mut tables = vec![vec![0; m + 1]; n + 1];

        for i in 0..n + 1 {
            for j in 0..m + 1 {
                if i == 0 || j == 0 {
                    tables[i][j] = 0;
                } else if c1[i - 1] == c2[j - 1] {
                    tables[i][j] = 1 + tables[i - 1][j - 1];
                } else {
                    tables[i][j] = std::cmp::max(tables[i - 1][j], tables[i][j - 1]);
                }
            }
        }

        return tables[n][m];
    }

    pub fn longest_common_subsequence_rec_cache(text1: String, text2: String) -> i32 {
        let n = text1.len();
        let m = text2.len();
        let mut cache = vec![vec![0; m + 1]; n + 1];

        Self::rec_helper_cache(
            text1.len(),
            text2.len(),
            &text1.chars().collect::<Vec<char>>(),
            &text2.chars().collect::<Vec<char>>(),
            &mut cache,
        ) as i32
    }

    fn rec_helper_cache(
        i: usize,
        j: usize,
        c1: &[char],
        c2: &[char],
        cache: &mut Vec<Vec<usize>>,
    ) -> usize {
        if cache[i][j] != 0 {
            return cache[i][j];
        }

        if i == 0 || j == 0 {
            return 0;
        }

        if c1[i - 1] == c2[j - 1] {
            cache[i][j] = 1 + Self::rec_helper_cache(i - 1, j - 1, c1, c2, cache);

            return cache[i][j];
        }

        cache[i][j] = std::cmp::max(
            Self::rec_helper_cache(i - 1, j, c1, c2, cache),
            Self::rec_helper_cache(i, j - 1, c1, c2, cache),
        );

        return cache[i][j];
    }

    pub fn longest_common_subsequence_rec(text1: String, text2: String) -> i32 {
        Self::rec_helper(
            text1.len(),
            text2.len(),
            &text1.chars().collect::<Vec<char>>(),
            &text2.chars().collect::<Vec<char>>(),
        )
    }

    fn rec_helper(i: usize, j: usize, c1: &[char], c2: &[char]) -> i32 {
        if i == 0 || j == 0 {
            return 0;
        }

        if c1[i - 1] == c2[j - 1] {
            return 1 + Self::rec_helper(i - 1, j - 1, c1, c2);
        }

        return std::cmp::max(
            Self::rec_helper(i - 1, j, c1, c2),
            Self::rec_helper(i, j - 1, c1, c2),
        );
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let text1 = "abcde".to_string();
        let text2 = "ace".to_string();
        let expected = 3;

        // act
        let actual = Solution::longest_common_subsequence(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let text1 = "abc".to_string();
        let text2 = "abc".to_string();
        let expected = 3;

        // act
        let actual = Solution::longest_common_subsequence(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        // arrange
        let text1 = "abc".to_string();
        let text2 = "def".to_string();
        let expected = 0;

        // act
        let actual = Solution::longest_common_subsequence(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        // arrange
        let text1 = "abcde".to_string();
        let text2 = "ace".to_string();
        let expected = 3;

        // act
        let actual = Solution::longest_common_subsequence_rec(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        // arrange
        let text1 = "abc".to_string();
        let text2 = "abc".to_string();
        let expected = 3;

        // act
        let actual = Solution::longest_common_subsequence_rec(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        // arrange
        let text1 = "abc".to_string();
        let text2 = "def".to_string();
        let expected = 0;

        // act
        let actual = Solution::longest_common_subsequence_rec(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_7() {
        // arrange
        let text1 = "abcde".to_string();
        let text2 = "ace".to_string();
        let expected = 3;

        // act
        let actual = Solution::longest_common_subsequence_rec_cache(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_8() {
        // arrange
        let text1 = "abc".to_string();
        let text2 = "abc".to_string();
        let expected = 3;

        // act
        let actual = Solution::longest_common_subsequence_rec_cache(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_9() {
        // arrange
        let text1 = "abc".to_string();
        let text2 = "def".to_string();
        let expected = 0;

        // act
        let actual = Solution::longest_common_subsequence_rec_cache(text1, text2);

        // assert
        assert_eq!(expected, actual);
    }
}
