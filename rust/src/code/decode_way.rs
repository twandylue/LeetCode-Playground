use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    // NOTE: in DP
    pub fn num_decodings_dp(s: String) -> i32 {
        let s = s.chars().collect::<Vec<char>>();
        let mut dp: HashMap<usize, i32> = HashMap::from([(s.len(), 1)]);
        let special_char_set = HashSet::from(['0', '1', '2', '3', '4', '5', '6']);
        for i in (0..s.len()).rev() {
            if s[i] == '0' {
                dp.insert(i, 0);
            } else {
                dp.insert(i, dp[&(i + 1)]);
            }

            if i + 1 < s.len()
                && (s[i] == '1' || (s[i] == '2' && special_char_set.contains(&s[i + 1])))
            {
                let value = dp[&(i + 2)];
                dp.entry(i).and_modify(|e| *e += value);
            }
        }
        return dp[&0];
    }

    // NOTE: in DFS
    pub fn num_decodings(s: String) -> i32 {
        let s = s.chars().collect::<Vec<char>>();
        let special_char_set = HashSet::from(['0', '1', '2', '3', '4', '5', '6']);
        let mut dp: HashMap<usize, i32> = HashMap::from([(s.len(), 1)]);

        return Self::dfs(0, &s, &mut dp, &special_char_set);
    }

    fn dfs(
        i: usize,
        s: &Vec<char>,
        dp: &mut HashMap<usize, i32>,
        special_char_set: &HashSet<char>,
    ) -> i32 {
        if dp.contains_key(&i) {
            return dp[&i];
        }
        if i >= s.len() {
            return 0;
        }
        if s[i] == '0' {
            return 0;
        }

        let mut result = 0;
        result += Self::dfs(i + 1, s, dp, special_char_set);

        if s[i] == '1' || (i < s.len() - 1 && s[i] == '2' && special_char_set.contains(&s[i + 1])) {
            result += Self::dfs(i + 2, s, dp, special_char_set);
        }

        dp.entry(i).or_insert(result);
        return result;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn num_decodings_case_1() {
        // arrange
        let s = "12".to_string();
        let expected = 2;

        // act
        let actual = Solution::num_decodings(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_2() {
        // arrange
        let s = "226".to_string();
        let expected = 3;

        // act
        let actual = Solution::num_decodings(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_3() {
        // arrange
        let s = "06".to_string();
        let expected = 0;

        // act
        let actual = Solution::num_decodings(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_4() {
        // arrange
        let s = "1".to_string();
        let expected = 1;

        // act
        let actual = Solution::num_decodings(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_5() {
        // arrange
        let s = "12".to_string();
        let expected = 2;

        // act
        let actual = Solution::num_decodings_dp(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_6() {
        // arrange
        let s = "226".to_string();
        let expected = 3;

        // act
        let actual = Solution::num_decodings_dp(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_7() {
        // arrange
        let s = "06".to_string();
        let expected = 0;

        // act
        let actual = Solution::num_decodings_dp(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn num_decodings_case_8() {
        // arrange
        let s = "1".to_string();
        let expected = 1;

        // act
        let actual = Solution::num_decodings_dp(s);

        // assert
        assert_eq!(expected, actual);
    }
}
