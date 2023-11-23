struct Solution {}

impl Solution {
    pub fn max_product(s: String) -> i32 {
        use std::collections::HashMap;
        let s: Vec<char> = s.chars().collect();
        let n: usize = s.len();
        let mut pali: HashMap<i32, i32> = HashMap::new();

        for mask in 1..(1 << n) {
            let mut subseq: Vec<char> = Vec::new();
            for i in 0..n {
                if (mask & (1 << i)) > 0 {
                    subseq.push(s[i]);
                }
            }

            if Self::is_pali(&subseq) {
                pali.entry(mask)
                    .and_modify(|x| *x = subseq.len() as i32)
                    .or_insert(subseq.len() as i32);
            }
        }

        let mut result: i32 = 0;
        for (m1, l1) in &pali {
            for (m2, l2) in &pali {
                if m1 & m2 == 0 {
                    result = std::cmp::max(result, l1 * l2);
                }
            }
        }

        result
    }

    fn is_pali(s: &Vec<char>) -> bool {
        if s.len() == 0 {
            return true;
        }

        let mut r: usize = 0;
        let mut l: usize = s.len() - 1;
        while r < l {
            if s[r] == s[l] {
                r += 1;
                l -= 1;
            } else {
                return false;
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn max_product_case_1() {
        // arrange
        let s: String = "leetcodecom".to_string();
        let expected: i32 = 9;

        // act
        let actual = Solution::max_product(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn max_product_case_2() {
        // arrange
        let s: String = "bb".to_string();
        let expected: i32 = 1;

        // act
        let actual = Solution::max_product(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn max_product_case_3() {
        // arrange
        let s: String = "accbcaxxcxx".to_string();
        let expected: i32 = 25;

        // act
        let actual = Solution::max_product(s);

        // assert
        assert_eq!(expected, actual);
    }
}
