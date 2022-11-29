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
use std::collections::VecDeque;
use std::mem;
use std::rc::Rc;

pub struct Solution {}

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        Solution::bfs(&root);
        root
    }

    fn bfs(root: &Option<Rc<RefCell<TreeNode>>>) {
        if let Some(n) = root {
            Solution::bfs(&n.borrow().left);
            Solution::bfs(&n.borrow().right);
            let tree = &mut *n.borrow_mut();
            mem::swap(&mut tree.left, &mut tree.right)
        }
    }

    pub fn invert_tree_2(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        if let Some(n) = root {
            let left = n.borrow().left.clone();
            let right = n.borrow().right.clone();
            n.borrow_mut().left = Solution::invert_tree_2(right);
            n.borrow_mut().right = Solution::invert_tree_2(left);
            Some(n)
        } else {
            None
        }
    }

    pub fn invert_tree_3(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut stack: Vec<Option<Rc<RefCell<TreeNode>>>> = vec![root.clone()];
        while let Some(ele) = stack.pop() {
            if let Some(n) = ele {
                {
                    let tree = &mut *n.borrow_mut();
                    mem::swap(&mut tree.left, &mut tree.right);
                }
                stack.push(n.borrow().right.clone());
                stack.push(n.borrow().left.clone());
            }
        }

        root
    }

    pub fn invert_tree_4(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::from(vec![root.clone()]);
        while let Some(ele) = queue.pop_front() {
            if let Some(n) = ele {
                {
                    let tree = &mut *n.borrow_mut();
                    mem::swap(&mut tree.left, &mut tree.right);
                }
                queue.push_back(n.borrow().left.clone());
                queue.push_back(n.borrow().right.clone());
            }
        }

        root
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn invert_tree_cases() {
        let input_tree = self::convert_to_tree_bfs(&vec![4, 2, 7, 1, 3, 6, 9], 0);
        let expected_tree = self::convert_to_tree_bfs(&vec![4, 7, 2, 9, 6, 3, 1], 0);
        let actual = Solution::invert_tree(input_tree);

        let input_tree2 = self::convert_to_tree_bfs(&vec![2, 1, 3], 0);
        let expected_tree2 = self::convert_to_tree_bfs(&vec![2, 3, 1], 0);
        let actual2 = Solution::invert_tree(input_tree2);

        let input_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let expected_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let actual3 = Solution::invert_tree(input_tree3);

        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    #[test]
    fn invert_tree_2_cases() {
        let input_tree = self::convert_to_tree_bfs(&vec![4, 2, 7, 1, 3, 6, 9], 0);
        let expected_tree = self::convert_to_tree_bfs(&vec![4, 7, 2, 9, 6, 3, 1], 0);
        let actual = Solution::invert_tree_2(input_tree);

        let input_tree2 = self::convert_to_tree_bfs(&vec![2, 1, 3], 0);
        let expected_tree2 = self::convert_to_tree_bfs(&vec![2, 3, 1], 0);
        let actual2 = Solution::invert_tree_2(input_tree2);

        let input_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let expected_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let actual3 = Solution::invert_tree_2(input_tree3);

        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    #[test]
    fn invert_tree_3_cases() {
        let input_tree = self::convert_to_tree_bfs(&vec![4, 2, 7, 1, 3, 6, 9], 0);
        let expected_tree = self::convert_to_tree_bfs(&vec![4, 7, 2, 9, 6, 3, 1], 0);
        let actual = Solution::invert_tree_3(input_tree);

        let input_tree2 = self::convert_to_tree_bfs(&vec![2, 1, 3], 0);
        let expected_tree2 = self::convert_to_tree_bfs(&vec![2, 3, 1], 0);
        let actual2 = Solution::invert_tree_3(input_tree2);

        let input_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let expected_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let actual3 = Solution::invert_tree_3(input_tree3);

        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    #[test]
    fn invert_tree_4_cases() {
        let input_tree = self::convert_to_tree_bfs(&vec![4, 2, 7, 1, 3, 6, 9], 0);
        let expected_tree = self::convert_to_tree_bfs(&vec![4, 7, 2, 9, 6, 3, 1], 0);
        let actual = Solution::invert_tree_4(input_tree);

        let input_tree2 = self::convert_to_tree_bfs(&vec![2, 1, 3], 0);
        let expected_tree2 = self::convert_to_tree_bfs(&vec![2, 3, 1], 0);
        let actual2 = Solution::invert_tree_4(input_tree2);

        let input_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let expected_tree3 = self::convert_to_tree_bfs(&vec![], 0);
        let actual3 = Solution::invert_tree_4(input_tree3);

        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    fn convert_to_tree_bfs(input: &Vec<i32>, index: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if index > input.len() as i32 - 1 {
            return None;
        }
        let mut node = TreeNode::new(input[index as usize]);
        node.left = self::convert_to_tree_bfs(input, 2 * index + 1);
        node.right = self::convert_to_tree_bfs(input, 2 * index + 2);
        return Some(Rc::new(RefCell::new(node)));
    }

    // in sorted array(LC 108)
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
