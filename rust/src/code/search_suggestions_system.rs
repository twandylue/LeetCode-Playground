struct Solution {}

impl Solution {
    // NOTE: time complexity: O(nlogn + m + n), where n is the length of products and m is the
    // length of search_word.
    pub fn suggested_products(mut products: Vec<String>, search_word: String) -> Vec<Vec<String>> {
        let mut result: Vec<Vec<String>> = Vec::new();
        products.sort();
        let search_word: Vec<char> = search_word.chars().collect();
        let products: Vec<Vec<char>> = products.into_iter().map(|s| s.chars().collect()).collect();
        let mut l: usize = 0;
        let mut r: usize = products.len() - 1;
        for i in 0..search_word.len() {
            let c: char = search_word[i];
            while l <= r && (products[l].len() <= i || products[l][i] != c) {
                l += 1;
            }
            // if r.checked_sub(1).is_none() {
            //     break;
            // }
            while l <= r && (products[r].len() <= i || products[r][i] != c) {
                r -= 1;
            }
            let curr_len: usize = r - l + 1;
            if curr_len >= 3 {
                result.push(
                    products[l..l + 3]
                        .iter()
                        .map(|v| v.iter().collect())
                        .collect(),
                );
            } else {
                result.push(
                    products[l..r + 1]
                        .iter()
                        .map(|v| v.iter().collect())
                        .collect(),
                );
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_suggested_products_case_1() {
        // arrange
        let products: Vec<String> = vec![
            "mobile".to_string(),
            "mouse".to_string(),
            "moneypot".to_string(),
            "monitor".to_string(),
            "mousepad".to_string(),
        ];
        let search_word: String = "mouse".to_string();
        let expected: Vec<Vec<String>> = vec![
            vec![
                "mobile".to_string(),
                "moneypot".to_string(),
                "monitor".to_string(),
            ],
            vec![
                "mobile".to_string(),
                "moneypot".to_string(),
                "monitor".to_string(),
            ],
            vec!["mouse".to_string(), "mousepad".to_string()],
            vec!["mouse".to_string(), "mousepad".to_string()],
            vec!["mouse".to_string(), "mousepad".to_string()],
        ];

        // act
        let actual = Solution::suggested_products(products, search_word);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_suggested_products_case_2() {
        // arrange
        let products: Vec<String> = vec!["havana".to_string()];
        let search_word: String = "havana".to_string();
        let expected: Vec<Vec<String>> = vec![
            vec!["havana".to_string()],
            vec!["havana".to_string()],
            vec!["havana".to_string()],
            vec!["havana".to_string()],
            vec!["havana".to_string()],
            vec!["havana".to_string()],
        ];

        // act
        let actual = Solution::suggested_products(products, search_word);

        // assert
        assert_eq!(expected, actual);
    }
}
