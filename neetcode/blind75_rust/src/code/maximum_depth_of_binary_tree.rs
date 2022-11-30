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
use std::cmp;
use std::rc::Rc;

pub struct Solution {}

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Solution::dfs(&root, 0)
    }

    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, mut count: i32) -> i32 {
        if let Some(n) = root {
            count += 1;
            let l = Solution::dfs(&n.borrow().left, count);
            let r = Solution::dfs(&n.borrow().right, count);
            cmp::max(l, r)
        } else {
            count
        }
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let root = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let root_tree = self::convert_to_tree_bfs(&root, 0);
        let expected = 3;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = vec![Some(1), None, Some(2)];
        let root_tree = self::convert_to_tree_bfs(&root, 0);
        let expected = 2;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let root = vec![Some(0)];
        let root_tree = self::convert_to_tree_bfs(&root, 0);
        let expected = 1;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let root = vec![];
        let root_tree = self::convert_to_tree_bfs(&root, 0);
        let expected = 0;
        let actual = Solution::max_depth(root_tree);

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
