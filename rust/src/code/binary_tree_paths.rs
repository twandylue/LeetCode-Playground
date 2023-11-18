// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
//
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use super::models::binary_tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution {}

impl Solution {
    pub fn binary_tree_paths(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        use std::collections::VecDeque;
        let mut q: VecDeque<(Option<Rc<RefCell<TreeNode>>>, String)> = VecDeque::new();
        if let Some(r) = root.as_ref() {
            q.push_back((Some(Rc::clone(r)), r.borrow().val.to_string()));
        }
        let mut paths = Vec::new();

        while !q.is_empty() {
            if let Some((current_node, path)) = q.pop_front() {
                match current_node {
                    Some(n) => {
                        if n.borrow().left == None && n.borrow().right == None {
                            paths.push(path);
                            continue;
                        }
                        if let Some(ln) = n.borrow().left.as_ref() {
                            let mut left_path: String = path.clone() + "->";
                            left_path.push_str(&ln.borrow().val.to_string());
                            q.push_back((Some(Rc::clone(ln)), left_path));
                        }
                        if let Some(rn) = &n.borrow().right.as_ref() {
                            let mut right_path: String = path.clone() + "->";
                            right_path.push_str(&rn.borrow().val.to_string());
                            q.push_back((Some(Rc::clone(rn)), right_path));
                        }
                    }
                    None => {}
                }
            }
        }

        paths
    }

    pub fn binary_tree_paths_dfs_recur(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        let mut paths: Vec<String> = Vec::new();
        let mut path: Vec<i32> = Vec::new();

        Self::dfs_recur_helper(root, &mut path, &mut paths);

        paths
    }

    fn dfs_recur_helper(
        node: Option<Rc<RefCell<TreeNode>>>,
        path: &mut Vec<i32>,
        paths: &mut Vec<String>,
    ) {
        if let Some(n) = node {
            path.push(n.borrow().val);
            if n.borrow().left.is_none() && n.borrow().right.is_none() {
                let p: String = path
                    .iter()
                    .map(|i| i.to_string())
                    .collect::<Vec<String>>()
                    .join("->");
                paths.push(p);
                return;
            }

            Self::dfs_recur_helper(n.borrow().left.clone(), path, paths);
            if n.borrow().left.is_some() {
                path.pop();
            }
            Self::dfs_recur_helper(n.borrow().right.clone(), path, paths);
            if n.borrow().right.is_some() {
                path.pop();
            }
        }
    }

    pub fn binary_tree_paths_dfs_iter(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<String> {
        let mut paths: Vec<String> = Vec::new();
        let mut stack: Vec<(Option<Rc<RefCell<TreeNode>>>, Vec<i32>)> = Vec::new();

        if let Some(root) = root {
            stack.push((Some(root), Vec::new()));
        } else {
            return paths;
        }

        while let Some((current_node, mut current_path)) = stack.pop() {
            match current_node {
                Some(n) => {
                    current_path.push(n.borrow().val);
                    if n.borrow().right.is_none() && n.borrow().left.is_none() {
                        let p: String = current_path
                            .iter()
                            .map(|i| i.to_string())
                            .collect::<Vec<String>>()
                            .join("->");
                        paths.push(p);
                    }

                    if let Some(right) = n.borrow().right.clone() {
                        stack.push((Some(right.clone()), current_path.clone()));
                    }
                    if let Some(left) = n.borrow().left.clone() {
                        stack.push((Some(left.clone()), current_path.clone()));
                    }
                }
                _ => {
                    break;
                }
            }
        }

        paths
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    #[test]
    fn binary_tree_paths_case_1() {
        // arrange
        let root = vec![Some(1), Some(2), Some(3), None, Some(5)];
        let p_tree = deserialize_to_BT(root);
        let mut expected: Vec<String> = vec!["1->2->5".to_string(), "1->3".to_string()];

        // act
        let mut actual = Solution::binary_tree_paths(p_tree);

        // assert
        expected.sort_by(|a, b| a.len().cmp(&b.len()));
        actual.sort_by(|a, b| a.len().cmp(&b.len()));
        assert_eq!(expected, actual);
    }

    #[test]
    fn binary_tree_paths_case_2() {
        // arrange
        let root = vec![Some(1)];
        let p_tree = deserialize_to_BT(root);
        let mut expected: Vec<String> = vec!["1".to_string()];

        // act
        let mut actual = Solution::binary_tree_paths(p_tree);

        // assert
        expected.sort_by(|a, b| a.len().cmp(&b.len()));
        actual.sort_by(|a, b| a.len().cmp(&b.len()));
        assert_eq!(expected, actual);
    }

    #[test]
    fn binary_tree_paths_case_3() {
        // arrange
        let root = vec![Some(1), Some(2), Some(3), None, Some(5)];
        let p_tree = deserialize_to_BT(root);
        let mut expected: Vec<String> = vec!["1->2->5".to_string(), "1->3".to_string()];

        // act
        let mut actual = Solution::binary_tree_paths_dfs_recur(p_tree);

        // assert
        expected.sort_by(|a, b| a.len().cmp(&b.len()));
        actual.sort_by(|a, b| a.len().cmp(&b.len()));
        assert_eq!(expected, actual);
    }

    #[test]
    fn binary_tree_paths_case_4() {
        // arrange
        let root = vec![Some(1)];
        let p_tree = deserialize_to_BT(root);
        let mut expected: Vec<String> = vec!["1".to_string()];

        // act
        let mut actual = Solution::binary_tree_paths_dfs_recur(p_tree);

        // assert
        expected.sort_by(|a, b| a.len().cmp(&b.len()));
        actual.sort_by(|a, b| a.len().cmp(&b.len()));
        assert_eq!(expected, actual);
    }

    #[test]
    fn binary_tree_paths_case_5() {
        // arrange
        let root = vec![Some(1), Some(2), Some(3), None, Some(5)];
        let p_tree = deserialize_to_BT(root);
        let mut expected: Vec<String> = vec!["1->2->5".to_string(), "1->3".to_string()];

        // act
        let mut actual = Solution::binary_tree_paths_dfs_iter(p_tree);

        // assert
        expected.sort_by(|a, b| a.len().cmp(&b.len()));
        actual.sort_by(|a, b| a.len().cmp(&b.len()));
        assert_eq!(expected, actual);
    }

    #[test]
    fn binary_tree_paths_case_6() {
        // arrange
        let root = vec![Some(1)];
        let p_tree = deserialize_to_BT(root);
        let mut expected: Vec<String> = vec!["1".to_string()];

        // act
        let mut actual = Solution::binary_tree_paths_dfs_iter(p_tree);

        // assert
        expected.sort_by(|a, b| a.len().cmp(&b.len()));
        actual.sort_by(|a, b| a.len().cmp(&b.len()));
        assert_eq!(expected, actual);
    }
}
