use std::collections::{HashMap, HashSet, VecDeque};

struct Solution {}

impl Solution {
    // NOTE: time complexity O(n^2 * m) where n is the length of word_list and m is the length of each word
    pub fn ladder_length(begin_word: String, end_word: String, mut word_list: Vec<String>) -> i32 {
        if !word_list.contains(&end_word) {
            return 0;
        }

        let mut result = 1;
        word_list.push(begin_word.clone());
        let mut queue: VecDeque<String> = VecDeque::from([begin_word.clone()]);
        let mut visited: HashSet<String> = HashSet::from([begin_word.clone()]);
        let mut adj_words: HashMap<String, Vec<String>> = HashMap::new();
        for word in word_list {
            let word: Vec<char> = word.chars().collect::<Vec<char>>();
            for i in 0..word.len() {
                let mut pattern: String = String::new();
                pattern.push_str(word[..i].iter().collect::<String>().as_str());
                pattern.push('*');
                pattern.push_str(word[i + 1..].iter().collect::<String>().as_str());
                adj_words
                    .entry(pattern)
                    .and_modify(|x| x.push(word.iter().collect::<String>()))
                    .or_insert(vec![word.iter().collect::<String>()]);
            }
        }

        while !queue.is_empty() {
            for _ in 0..queue.len() {
                if let Some(word) = queue.pop_front() {
                    if word == end_word {
                        return result;
                    }

                    let word: Vec<char> = word.chars().collect::<Vec<char>>();
                    for i in 0..word.len() {
                        let mut pattern: String = String::new();
                        pattern.push_str(word[..i].iter().collect::<String>().as_str());
                        pattern.push('*');
                        pattern.push_str(word[i + 1..].iter().collect::<String>().as_str());

                        if let Some(next_words) = adj_words.get(&pattern) {
                            for next_word in next_words {
                                if !visited.contains(next_word) {
                                    visited.insert(next_word.clone());
                                    queue.push_back(next_word.clone());
                                }
                            }
                        } else {
                            unreachable!("should not reach here");
                        }
                    }
                } else {
                    unreachable!("should not reach here");
                }
            }

            result += 1;
        }

        return 0;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn ladder_length_case_1() {
        // arrange
        let begin_word: String = "hit".to_string();
        let end_word: String = "cog".to_string();
        let word_list: Vec<String> = vec![
            "hot".to_string(),
            "dot".to_string(),
            "dog".to_string(),
            "lot".to_string(),
            "log".to_string(),
            "cog".to_string(),
        ];
        let expected: i32 = 5;

        // act
        let actual = Solution::ladder_length(begin_word, end_word, word_list);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn ladder_length_case_2() {
        // arrange
        let begin_word: String = "hit".to_string();
        let end_word: String = "cog".to_string();
        let word_list: Vec<String> = vec![
            "hot".to_string(),
            "dot".to_string(),
            "dog".to_string(),
            "lot".to_string(),
            "log".to_string(),
        ];
        let expected: i32 = 0;

        // act
        let actual = Solution::ladder_length(begin_word, end_word, word_list);

        // assert
        assert_eq!(actual, expected);
    }
}
