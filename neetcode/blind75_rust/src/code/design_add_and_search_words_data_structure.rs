use std::collections::HashMap;

struct WordDictionary {
    root: Node,
}

#[derive(Debug, Clone)]
struct Node {
    map: HashMap<char, Node>,
}

impl Node {
    pub fn new() -> Self {
        Node {
            map: HashMap::new(),
        }
    }
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {
    fn new() -> Self {
        WordDictionary { root: Node::new() }
    }

    fn add_word(&mut self, word: String) {
        let mut p = &mut self.root;
        for c in word.chars() {
            if !p.map.contains_key(&c) {
                p.map.insert(c, Node::new());
            }
            p = p.map.get_mut(&c).unwrap();
        }
        p.map.insert('#', Node::new());
    }

    fn search(&self, word: String) -> bool {
        WordDictionary::find(&self, &self.root, &word)
    }

    fn find(&self, node: &Node, word: &str) -> bool {
        if word.is_empty() {
            match node.map.get(&'#') {
                Some(_) => return true,
                None => return false,
            };
        }

        if word.chars().nth(0).unwrap() == '.' {
            for (k, v) in node.map.iter() {
                if *k != '#' && self.find(v, &word[1..]) {
                    return true;
                }
            }
        } else {
            match node.map.get(&word.chars().nth(0).unwrap()) {
                Some(n) => return self.find(n, &word[1..]),
                None => return false,
            };
        };

        return false;
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */

#[cfg(test)]
mod tests {
    use super::WordDictionary;

    #[test]
    fn case_1() {
        let mut word_dictionary = WordDictionary::new();
        word_dictionary.add_word("bad".to_string());
        word_dictionary.add_word("dad".to_string());
        word_dictionary.add_word("mad".to_string());
        assert_eq!(false, word_dictionary.search("pad".to_string())); // return False
        assert_eq!(true, word_dictionary.search("bad".to_string())); // return True
        assert_eq!(true, word_dictionary.search(".ad".to_string())); // return True
        assert_eq!(true, word_dictionary.search("b..".to_string())); // return True
    }

    #[test]
    fn case_2() {
        let mut word_dictionary = WordDictionary::new();
        word_dictionary.add_word("at".to_string());
        word_dictionary.add_word("and".to_string());
        word_dictionary.add_word("an".to_string());
        word_dictionary.add_word("add".to_string());
        assert_eq!(false, word_dictionary.search("a".to_string()));
        assert_eq!(false, word_dictionary.search(".at".to_string()));
        word_dictionary.add_word("bat".to_string());
        assert_eq!(true, word_dictionary.search(".at".to_string()));
        assert_eq!(true, word_dictionary.search("an.".to_string()));
        assert_eq!(false, word_dictionary.search("a.d.".to_string()));
        assert_eq!(false, word_dictionary.search("b.".to_string()));
        assert_eq!(true, word_dictionary.search("a.d".to_string()));
        assert_eq!(false, word_dictionary.search(".".to_string()));
    }
}
