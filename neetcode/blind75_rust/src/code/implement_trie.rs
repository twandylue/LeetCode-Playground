use std::collections::HashMap;

#[derive(PartialEq, Eq, Debug, Clone)]
struct Node {
    map: HashMap<char, Node>,
}

impl Node {
    fn new() -> Self {
        Node {
            map: HashMap::<char, Node>::new(),
        }
    }
}

struct Trie {
    root: Node,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Trie {
    fn new() -> Self {
        Trie { root: Node::new() }
    }

    fn insert(&mut self, word: String) {
        let mut p = &mut self.root;

        for c in word.chars() {
            if !p.map.contains_key(&c) {
                p.map.insert(c, Node::new());
            }
            p = p.map.get_mut(&c).unwrap();
        }

        p.map.insert('&', Node::new());
    }

    fn search(&self, word: String) -> bool {
        match Trie::find(self, word) {
            Some(node) => {
                println!("{:?}", node);
                if node.map.contains_key(&'&') {
                    true
                } else {
                    false
                }
            }
            None => false,
        }
    }

    fn starts_with(&mut self, prefix: String) -> bool {
        match Trie::find(self, prefix) {
            Some(_) => true,
            None => false,
        }
    }

    fn find(&self, prefix: String) -> Option<Node> {
        let mut p = &self.root;
        for c in prefix.chars() {
            if !p.map.contains_key(&c) {
                return None;
            }
            p = p.map.get(&c).unwrap();
        }

        return Some(p.clone());
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * let obj = Trie::new();
 * obj.insert(word);
 * let ret_2: bool = obj.search(word);
 * let ret_3: bool = obj.starts_with(prefix);
 */

#[cfg(test)]
mod tests {
    use super::Trie;

    #[test]
    fn case_1() {
        let mut t = Trie::new();
        t.insert("andy".to_string());

        let expected = true;
        assert_eq!(expected, t.starts_with("a".to_string()));
        assert_eq!(expected, t.starts_with("and".to_string()));
        assert_eq!(expected, t.starts_with("andy".to_string()));
    }

    #[test]
    fn case_2() {
        let mut t = Trie::new();
        t.insert("apple".to_string());

        assert_eq!(true, t.search("apple".to_string()));
        assert_eq!(false, t.search("app".to_string()));
        assert_eq!(true, t.starts_with("app".to_string()));

        t.insert("app".to_string());
        assert_eq!(true, t.search("app".to_string()));
    }
}
