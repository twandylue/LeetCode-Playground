struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn is_isomorphic(s: String, t: String) -> bool {
        use std::collections::HashMap;

        let s: Vec<char> = s.chars().collect();
        let t: Vec<char> = t.chars().collect();
        if s.len() != t.len() {
            return false;
        }
        let mut s_t_map: HashMap<char, char> = HashMap::new();
        let mut t_s_map: HashMap<char, char> = HashMap::new();
        for i in 0..s.len() {
            if let Some(c) = s_t_map.get(&s[i]) {
                if *c != t[i] {
                    return false;
                }
            } else {
                s_t_map.insert(s[i], t[i]);
            }
            if let Some(c) = t_s_map.get(&t[i]) {
                if *c != s[i] {
                    return false;
                }
            } else {
                t_s_map.insert(t[i], s[i]);
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_isomorphic_case_1() {
        // arrange
        let s: String = "egg".to_string();
        let t: String = "add".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::is_isomorphic(s, t);

        // assert
        assert_eq!(expected, actual);
    }
}
