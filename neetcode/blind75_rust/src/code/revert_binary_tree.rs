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
    // pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {}
}

#[cfg(test)]
mod tests {
    use std::{cell::RefCell, rc::Rc};

    use super::TreeNode;

    #[test]
    fn case_1() {
        let input = &vec![4, 2, 7, 1, 3, 6, 9];
        // let input = &vec![2, 1, 3];
        let input_tree = convert_to_tree(input, 0, 0);
        println!("{:?}", input_tree);
        let expected = &vec![4, 7, 2, 9, 6, 3, 1];
        // let expected_tree = convert_to_tree(expected, 0, (expected.len() - 1) as i32);
    }

    fn convert_to_tree(input: &Vec<i32>, start: i32, depth: i32) -> Option<Rc<RefCell<TreeNode>>> {
        // TODO:
        println!("index: {:?}", start);
        // println!("{:?}", input.len() as i32 - 1); // 6
        if start > input.len() as i32 - 1 {
            return None;
        }
        println!("val: {:?}", input[start as usize]);
        let base: i32 = 2;
        let gap = base.pow(depth as u32);
        let mut node = TreeNode::new(input[start as usize]);
        node.left = self::convert_to_tree(input, start + gap, depth + 1);
        node.right = self::convert_to_tree(input, start + gap + 1, depth + 1);
        return Some(Rc::new(RefCell::new(node)));
    }

    // in sorted array
    // fn convert_to_tree(input: &Vec<i32>, start: i32, end: i32) -> Option<Rc<RefCell<TreeNode>>> {
    //     if start > end {
    //         return None;
    //     }
    //     let mid = (start + end) / 2;
    //     let mut node = TreeNode::new(input[mid as usize]);
    //     node.left = self::convert_to_tree(input, start, mid - 1);
    //     node.right = self::convert_to_tree(input, mid + 1, end);
    //     return Some(Rc::new(RefCell::new(node)));
    // }
}
