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

#[derive(Debug)]
enum Action<T, U> {
    Call(T),
    Handler(U),
}

type NodeRef<T> = Option<Rc<RefCell<T>>>;

impl Solution {
    fn is_valid_bst_nonrecur(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let mut stack = Vec::<Action<(NodeRef<TreeNode>, i64, i64), ()>>::new();
        let mut ret_stack = Vec::<bool>::new();
        stack.push(Action::Call((root, i64::MIN, i64::MAX)));

        while let Some(action) = stack.pop() {
            match action {
                Action::Call(node) => {
                    if let (Some(n), min, max) = node {
                        if n.borrow().val as i64 <= min || n.borrow().val as i64 >= max {
                            ret_stack.push(false);
                            continue;
                        }
                        stack.push(Action::Handler(()));
                        stack.push(Action::Call((
                            n.borrow().right.clone(),
                            n.borrow().val as i64,
                            max,
                        )));
                        stack.push(Action::Call((
                            n.borrow().left.clone(),
                            min,
                            n.borrow().val as i64,
                        )));
                    } else {
                        ret_stack.push(true);
                    }
                }
                Action::Handler(()) => {
                    let r1 = ret_stack.pop().unwrap();
                    let r2 = ret_stack.pop().unwrap();
                    ret_stack.push(r1 && r2);
                }
            }
        }

        ret_stack.pop().unwrap()
    }

    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Solution::is_valid(&root, i64::MIN, i64::MAX)
    }

    fn is_valid(root: &Option<Rc<RefCell<TreeNode>>>, min: i64, max: i64) -> bool {
        match root {
            Some(node) => {
                if (node.borrow().val as i64 <= min) || (node.borrow().val as i64 >= max) {
                    return false;
                }

                Solution::is_valid(&node.borrow().left, min, node.borrow().val as i64)
                    && Solution::is_valid(&node.borrow().right, node.borrow().val as i64, max)
            }
            None => true,
        }
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_recur_1() {
        let root = self::convert_to_tree_bfs(&vec![Some(2), Some(1), Some(3)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_2() {
        let root = self::convert_to_tree_bfs(
            &vec![Some(5), Some(1), Some(4), None, None, Some(3), Some(6)],
            0,
        );
        let expected = false;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_3() {
        let root = self::convert_to_tree_bfs(&vec![Some(i32::MAX)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_4() {
        let root = self::convert_to_tree_bfs(&vec![Some(i32::MIN)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_5() {
        let root = self::convert_to_tree_bfs(&vec![Some(i32::MAX), Some(i32::MAX)], 0);
        let expected = false;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_6() {
        let root = self::convert_to_tree_bfs(&vec![Some(0)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_1() {
        let root = self::convert_to_tree_bfs(&vec![Some(2), Some(1), Some(3)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_2() {
        let root = self::convert_to_tree_bfs(
            &vec![Some(5), Some(1), Some(4), None, None, Some(3), Some(6)],
            0,
        );
        let expected = false;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_3() {
        let root = self::convert_to_tree_bfs(&vec![Some(i32::MAX)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_4() {
        let root = self::convert_to_tree_bfs(&vec![Some(i32::MIN)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_5() {
        let root = self::convert_to_tree_bfs(&vec![Some(i32::MAX), Some(i32::MAX)], 0);
        let expected = false;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_6() {
        let root = self::convert_to_tree_bfs(&vec![Some(0)], 0);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

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
