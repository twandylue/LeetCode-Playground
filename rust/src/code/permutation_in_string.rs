use std::collections::HashMap;

struct Solution {}

impl Solution {
    pub fn check_inclusion(s1: String, s2: String) -> bool {
        let mut s1_char_map: HashMap<char, usize> = HashMap::new();
        s1.chars().for_each(|c| {
            s1_char_map.entry(c).and_modify(|v| *v += 1).or_insert(1);
        });
        let s2_chars: Vec<char> = s2.chars().collect();
        let mut s2_win_char_map: HashMap<char, usize> = HashMap::new();

        let mut s: usize = 0;
        let mut e: usize = 0;

        while s <= e && e < s2.len() {
            if let Some(s1_v) = s1_char_map.get(&s2_chars[e]) {
                match s2_win_char_map.get_mut(&s2_chars[e]) {
                    Some(s2_v) => {
                        if *s2_v >= *s1_v {
                            // NOTE: move s(left)
                            s2_win_char_map.entry(s2_chars[s]).and_modify(|v| {
                                if *v >= 1 {
                                    *v -= 1
                                }
                            });
                            s += 1;
                        } else {
                            // NOTE: move e(right)
                            *s2_v += 1;
                            e += 1;
                        }
                    }
                    None => {
                        s2_win_char_map.insert(s2_chars[e], 1);
                        e += 1;
                    }
                }
            } else {
                let _ = s2_win_char_map.drain();
                e += 1;
                s = e;
            }

            if s1_char_map == s2_win_char_map {
                return true;
            }
        }

        false
    }

    pub fn check_inclusion_2(s1: String, s2: String) -> bool {
        if s1.len() > s2.len() {
            return false;
        }

        let s1_chars: Vec<char> = s1.chars().collect();
        let s2_chars: Vec<char> = s2.chars().collect();
        let mut matches = 0;
        let mut s1_count = [0; 26];
        let mut s2_count = [0; 26];
        for i in 0..s1_chars.len() {
            s1_count[(s1_chars[i] as u8 - 'a' as u8) as usize] += 1;
            s2_count[(s2_chars[i] as u8 - 'a' as u8) as usize] += 1;
        }

        for i in 0..26 {
            if s1_count[i] == s2_count[i] {
                matches += 1;
            }
        }

        let mut s = 0;
        for e in s1_chars.len()..s2_chars.len() {
            if matches == 26 {
                return true;
            }

            let index = (s2_chars[e] as u8 - 'a' as u8) as usize;
            s2_count[index] += 1;
            if s2_count[index] == s1_count[index] {
                matches += 1;
            } else if s2_count[index] == s1_count[index] + 1 {
                matches -= 1;
            }

            let index = (s2_chars[s] as u8 - 'a' as u8) as usize;
            s2_count[index] -= 1;
            if s2_count[index] == s1_count[index] {
                matches += 1;
            } else if s2_count[index] == s1_count[index] - 1 {
                matches -= 1;
            }

            s += 1;
        }

        return matches == 26;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn permutation_in_string_case_1() {
        // arrange
        let s1 = "ab".to_string();
        let s2 = "eidbaooo".to_string();
        let expected = true;

        // act
        let actual = Solution::check_inclusion(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_2() {
        // arrange
        let s1 = "ab".to_string();
        let s2 = "eidboaoo".to_string();
        let expected = false;

        // act
        let actual = Solution::check_inclusion(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_3() {
        // arrange
        let s1 = "adc".to_string();
        let s2 = "dcda".to_string();
        let expected = true;

        // act
        let actual = Solution::check_inclusion(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_4() {
        // arrange
        let s1 = "hello".to_string();
        let s2 = "ooolleoooleh".to_string();
        let expected = false;

        // act
        let actual = Solution::check_inclusion(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_5() {
        // arrange
        let s1 = "ab".to_string();
        let s2 = "eidbaooo".to_string();
        let expected = true;

        // act
        let actual = Solution::check_inclusion_2(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_6() {
        // arrange
        let s1 = "ab".to_string();
        let s2 = "eidboaoo".to_string();
        let expected = false;

        // act
        let actual = Solution::check_inclusion_2(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_7() {
        // arrange
        let s1 = "adc".to_string();
        let s2 = "dcda".to_string();
        let expected = true;

        // act
        let actual = Solution::check_inclusion_2(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn permutation_in_string_case_8() {
        // arrange
        let s1 = "hello".to_string();
        let s2 = "ooolleoooleh".to_string();
        let expected = false;

        // act
        let actual = Solution::check_inclusion_2(s1, s2);

        // assert
        assert_eq!(expected, actual);
    }
}
