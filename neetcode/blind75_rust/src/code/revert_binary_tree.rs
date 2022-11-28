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
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {}
}

#[cfg(test)]
mod tests {
    use super::TreeNode;

    #[test]
    fn case_1() {
        let root = vec![4, 2, 7, 1, 3, 6, 9];
        let expected = vec![4, 7, 2, 9, 6, 3, 1];
    }

    fn convert_to_tree(input: Vec<i32>) -> TreeNode {
        // TODO:
    }
}
