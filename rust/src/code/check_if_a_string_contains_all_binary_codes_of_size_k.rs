struct Solution {}

impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        use std::collections::HashSet;

        let s: Vec<char> = s.chars().collect();
        let k: usize = k as usize;
        if s.len() + 1 < k {
            return false;
        }

        let mut comb_set: HashSet<String> = HashSet::new();

        for i in 0..(s.len() - k + 1) {
            comb_set.insert(s[i..(i + k)].iter().collect::<String>());
        }

        return comb_set.len() == 2_i32.pow(k as u32) as usize;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn has_all_codes_case_1() {
        // arrange
        let s: String = "00110110".to_string();
        let k: i32 = 2;
        let expected = true;

        // act
        let actual = Solution::has_all_codes(s, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn has_all_codes_case_2() {
        // arrange
        let s: String = "0".to_string();
        let k: i32 = 20;
        let expected = false;

        // act
        let actual = Solution::has_all_codes(s, k);

        // assert
        assert_eq!(expected, actual);
    }
}
