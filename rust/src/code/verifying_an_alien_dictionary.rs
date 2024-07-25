struct Solution;

impl Solution {
    pub fn is_alien_sorted(words: Vec<String>, order: String) -> bool {
        use std::collections::HashMap;

        let order: Vec<char> = order.chars().collect();
        let mut order_idx: HashMap<char, usize> = HashMap::new();
        for i in 0..order.len() {
            order_idx.insert(order[i], i);
        }
        for i in 0..words.len() - 1 {
            let w1: Vec<char> = words[i].clone().chars().collect();
            let w2: Vec<char> = words[i + 1].clone().chars().collect();
            for j in 0..w1.len() {
                if j == w2.len() {
                    return false;
                }
                if w1[j] != w2[j] {
                    if order_idx[&w1[j]] > order_idx[&w2[j]] {
                        return false;
                    }
                    break;
                }
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_is_alien_sorted_case_1() {
        // arrange
        let words: Vec<String> = vec!["hello".to_string(), "leetcode".to_string()];
        let order: String = "hlabcdefgijkmnopqrstuvwxyz".to_string();
        let expected: bool = true;

        // act
        let actual = Solution::is_alien_sorted(words, order);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_is_alien_sorted_case_2() {
        // arrange
        let words: Vec<String> = vec!["word".to_string(), "world".to_string(), "row".to_string()];
        let order: String = "worldabcefghijkmnpqstuvxyz".to_string();
        let expected: bool = false;

        // act
        let actual = Solution::is_alien_sorted(words, order);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_is_alien_sorted_case_3() {
        // arrange
        let words: Vec<String> = vec!["apple".to_string(), "app".to_string()];
        let order: String = "abcdefghijklmnopqrstuvwxyz".to_string();
        let expected: bool = false;

        // act
        let actual = Solution::is_alien_sorted(words, order);

        // assert
        assert_eq!(expected, actual);
    }
}
