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
    pub fn build_tree(preorder: Vec<i32>, inorder: Vec<i32>) -> Option<Rc<RefCell<TreeNode>>> {
        if preorder.len() == 0 || inorder.len() == 0 {
            return None;
        }

        let m = inorder.iter().position(|&x| x == preorder[0]).unwrap();
        let root = Rc::new(RefCell::new(TreeNode::new(preorder[0])));
        root.borrow_mut().left =
            Solution::build_tree(preorder[1..(m + 1)].to_vec(), inorder[..m].to_vec());
        root.borrow_mut().right =
            Solution::build_tree(preorder[(m + 1)..].to_vec(), inorder[(m + 1)..].to_vec());

        return Some(root);
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let preorder = vec![3, 9, 20, 15, 7];
        let inorder = vec![9, 3, 15, 20, 7];
        let expected = self::convert_to_tree_bfs(
            &vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)],
            0,
        );

        let actual = Solution::build_tree(preorder, inorder);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let preorder = vec![-1];
        let inorder = vec![-1];
        let expected = self::convert_to_tree_bfs(&vec![Some(-1)], 0);
        let actual = Solution::build_tree(preorder, inorder);

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
