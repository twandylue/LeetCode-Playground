pub struct Solution {}

impl Solution {
    pub fn partition(s: String) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = Vec::new();
        let mut subset: Vec<String> = Vec::new();
        Self::dfs(0, &mut subset, &mut result, &s);

        result
    }

    fn dfs(pos: usize, subset: &mut Vec<String>, result: &mut Vec<Vec<String>>, s: &str) {
        if pos >= s.len() {
            result.push(subset.to_vec());
            return;
        }

        for i in pos..s.len() {
            if Self::is_pali(&s.chars().collect(), pos, i) {
                subset.push(s[pos..i + 1].to_string());
                Self::dfs(i + 1, subset, result, s);
                subset.pop().unwrap();
            }
        }
    }

    fn is_pali(s: &Vec<char>, mut l: usize, mut r: usize) -> bool {
        while l < r {
            if s[l] != s[r] {
                return false;
            }
            l += 1;

            if r > 0 {
                r -= 1;
            }
        }
        return true;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn partition_case_1() {
        // arrange
        let s: String = "aab".to_string();
        let expected: Vec<Vec<String>> = vec![
            vec!["a".to_string(), "a".to_string(), "b".to_string()],
            vec!["aa".to_string(), "b".to_string()],
        ];

        // act
        let actual: Vec<Vec<String>> = Solution::partition(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn partition_case_2() {
        // arrange
        let s: String = "a".to_string();
        let expected: Vec<Vec<String>> = vec![vec!["a".to_string()]];

        // act
        let actual: Vec<Vec<String>> = Solution::partition(s);

        // assert
        assert_eq!(expected, actual);
    }
}
