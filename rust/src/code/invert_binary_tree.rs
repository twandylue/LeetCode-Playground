use std::cell::RefCell;
use std::collections::VecDeque;
use std::mem;
use std::rc::Rc;

use super::models::binary_tree_node::TreeNode;

pub struct Solution {}

impl Solution {
    pub fn invert_tree(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        Solution::dfs(&root);
        root
    }

    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>) {
        if let Some(n) = root {
            Solution::dfs(&n.borrow().left);
            Solution::dfs(&n.borrow().right);
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
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn invert_tree_cases() {
        // arrange
        let input_tree = deserialize_to_BT(vec![
            Some(4),
            Some(2),
            Some(7),
            Some(1),
            Some(3),
            Some(6),
            Some(9),
        ]);
        let expected_tree = deserialize_to_BT(vec![
            Some(4),
            Some(7),
            Some(2),
            Some(9),
            Some(6),
            Some(3),
            Some(1),
        ]);

        // act
        let actual = Solution::invert_tree(input_tree);

        let input_tree2 = deserialize_to_BT(vec![Some(2), Some(1), Some(3)]);
        let expected_tree2 = deserialize_to_BT(vec![Some(2), Some(3), Some(1)]);
        let actual2 = Solution::invert_tree(input_tree2);

        let input_tree3 = deserialize_to_BT(vec![]);
        let expected_tree3 = deserialize_to_BT(vec![]);
        let actual3 = Solution::invert_tree(input_tree3);

        // assert
        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    #[test]
    fn invert_tree_2_cases() {
        // arrange
        let input_tree = deserialize_to_BT(vec![
            Some(4),
            Some(2),
            Some(7),
            Some(1),
            Some(3),
            Some(6),
            Some(9),
        ]);
        let expected_tree = deserialize_to_BT(vec![
            Some(4),
            Some(7),
            Some(2),
            Some(9),
            Some(6),
            Some(3),
            Some(1),
        ]);
        let actual = Solution::invert_tree_2(input_tree);

        let input_tree2 = deserialize_to_BT(vec![Some(2), Some(1), Some(3)]);
        let expected_tree2 = deserialize_to_BT(vec![Some(2), Some(3), Some(1)]);
        let actual2 = Solution::invert_tree_2(input_tree2);

        let input_tree3 = deserialize_to_BT(vec![]);
        let expected_tree3 = deserialize_to_BT(vec![]);
        let actual3 = Solution::invert_tree_2(input_tree3);

        // assert
        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    #[test]
    fn invert_tree_3_cases() {
        // arrange
        let input_tree = deserialize_to_BT(vec![
            Some(4),
            Some(2),
            Some(7),
            Some(1),
            Some(3),
            Some(6),
            Some(9),
        ]);
        let expected_tree = deserialize_to_BT(vec![
            Some(4),
            Some(7),
            Some(2),
            Some(9),
            Some(6),
            Some(3),
            Some(1),
        ]);

        // act
        let actual = Solution::invert_tree_3(input_tree);

        let input_tree2 = deserialize_to_BT(vec![Some(2), Some(1), Some(3)]);
        let expected_tree2 = deserialize_to_BT(vec![Some(2), Some(3), Some(1)]);
        let actual2 = Solution::invert_tree_3(input_tree2);

        let input_tree3 = deserialize_to_BT(vec![]);
        let expected_tree3 = deserialize_to_BT(vec![]);
        let actual3 = Solution::invert_tree_3(input_tree3);

        // assert
        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }

    #[test]
    fn invert_tree_4_cases() {
        // arrange
        let input_tree = deserialize_to_BT(vec![
            Some(4),
            Some(2),
            Some(7),
            Some(1),
            Some(3),
            Some(6),
            Some(9),
        ]);
        let expected_tree = deserialize_to_BT(vec![
            Some(4),
            Some(7),
            Some(2),
            Some(9),
            Some(6),
            Some(3),
            Some(1),
        ]);

        // act
        let actual = Solution::invert_tree_4(input_tree);

        let input_tree2 = deserialize_to_BT(vec![Some(2), Some(1), Some(3)]);
        let expected_tree2 = deserialize_to_BT(vec![Some(2), Some(3), Some(1)]);
        let actual2 = Solution::invert_tree_4(input_tree2);

        let input_tree3 = deserialize_to_BT(vec![]);
        let expected_tree3 = deserialize_to_BT(vec![]);
        let actual3 = Solution::invert_tree_4(input_tree3);

        // assert
        assert_eq!(expected_tree, actual);
        assert_eq!(expected_tree2, actual2);
        assert_eq!(expected_tree3, actual3);
    }
}
