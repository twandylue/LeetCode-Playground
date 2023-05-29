struct Solution {}

impl Solution {
    pub fn find_anagrams(s: String, p: String) -> Vec<i32> {
        if s.len() < p.len() {
            return Vec::<i32>::new();
        }

        let mut matches = 0;
        let mut result: Vec<i32> = Vec::new();
        let mut s_count = [0; 26];
        let mut p_count = [0; 26];
        let s_chars: Vec<char> = s.chars().collect();
        let p_chars: Vec<char> = p.chars().collect();

        for i in 0..p_chars.len() {
            p_count[(p_chars[i] as u8 - 'a' as u8) as usize] += 1;
            s_count[(s_chars[i] as u8 - 'a' as u8) as usize] += 1;
        }

        for i in 0..26 {
            if p_count[i] == s_count[i] {
                matches += 1;
            }
        }

        let mut s: usize = 0;
        for e in p_chars.len()..s_chars.len() {
            if matches == 26 {
                result.push(s as i32);
            }

            let index = (s_chars[e] as u8 - 'a' as u8) as usize;
            s_count[index] += 1;
            if p_count[index] == s_count[index] {
                matches += 1;
            } else if p_count[index] == s_count[index] - 1 {
                matches -= 1;
            }

            let index = (s_chars[s] as u8 - 'a' as u8) as usize;
            s_count[index] -= 1;
            if p_count[index] == s_count[index] {
                matches += 1;
            } else if p_count[index] == s_count[index] + 1 {
                matches -= 1;
            }

            s += 1;
        }

        if matches == 26 {
            result.push(s as i32);
        }

        result
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn find_anagrams_case_1() {
        // arrange
        let s = "cbaebabacd".to_string();
        let p = "abc".to_string();
        let expected = vec![0, 6];

        // act
        let actual = Solution::find_anagrams(s, p);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_anagrams_case_2() {
        // arrange
        let s = "abab".to_string();
        let p = "ab".to_string();
        let expected = vec![0, 1, 2];

        // act
        let actual = Solution::find_anagrams(s, p);

        // assert
        assert_eq!(expected, actual);
    }
}
