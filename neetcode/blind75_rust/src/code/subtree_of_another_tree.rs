// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

pub struct Solution {}

impl Solution {
    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        if Solution::same_tree(root.clone(), sub_root.clone()) {
            return true;
        }
        match (root, sub_root) {
            (Some(r), Some(s)) => {
                return Solution::is_subtree(r.borrow().left.clone(), Some(s.clone()))
                    || Solution::is_subtree(r.borrow().right.clone(), Some(s.clone()));
            }
            (_, None) => return true,
            (None, _) => return false,
        }
    }

    fn same_tree(s: Option<Rc<RefCell<TreeNode>>>, t: Option<Rc<RefCell<TreeNode>>>) -> bool {
        if s == None && t == None {
            return true;
        }

        match (s, t) {
            (Some(a), Some(b)) => {
                if a.borrow().val == b.borrow().val {
                    return Solution::same_tree(a.borrow().right.clone(), b.borrow().right.clone())
                        && Solution::same_tree(a.borrow().left.clone(), b.borrow().left.clone());
                }
                return false;
            }
            (_, _) => false,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let root = vec![Some(3), Some(4), Some(5), Some(1), Some(2)];
        let sub_root = vec![Some(4), Some(1), Some(2)];
        let expected = true;
        let actual = Solution::is_subtree(
            self::convert_to_tree_bfs(&root, 0),
            self::convert_to_tree_bfs(&sub_root, 0),
        );

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = vec![
            Some(3),
            Some(4),
            Some(5),
            Some(1),
            Some(2),
            None,
            None,
            None,
            None,
            Some(0),
        ];
        let sub_root = vec![Some(4), Some(1), Some(2)];
        let expected = false;
        let actual = Solution::is_subtree(
            self::convert_to_tree_bfs(&root, 0),
            self::convert_to_tree_bfs(&sub_root, 0),
        );

        assert_eq!(expected, actual);
    }

    fn convert_to_tree_bfs(input: &Vec<Option<i32>>, index: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if index > input.len() as i32 - 1 {
            return None;
        }
        if let Some(n) = input[index as usize] {
            let mut node = TreeNode::new(n);
            node.left = self::convert_to_tree_bfs(input, 2 * index + 1);
            node.right = self::convert_to_tree_bfs(input, 2 * index + 2);
            Some(Rc::new(RefCell::new(node)))
        } else {
            None
        }
    }
}
