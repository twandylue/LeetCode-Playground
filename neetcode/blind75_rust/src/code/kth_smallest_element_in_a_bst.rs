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

enum Action<T, U> {
    Caller(T),
    Handler(U),
}

impl Solution {
    pub fn kth_smallest_nonrecur(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut stack = Vec::<Action<Option<Rc<RefCell<TreeNode>>>, i32>>::new();
        let mut ret_stack = Vec::<i32>::new();
        stack.push(Action::Caller(root));
        while let Some(action) = stack.pop() {
            match action {
                Action::Caller(node) => {
                    if let Some(n) = node {
                        stack.push(Action::Caller(n.borrow().right.clone()));
                        stack.push(Action::Handler(n.borrow().val));
                        stack.push(Action::Caller(n.borrow().left.clone()));
                    }
                }
                Action::Handler(number) => {
                    ret_stack.push(number);
                }
            }
        }

        ret_stack[k as usize - 1]
    }

    pub fn kth_smallest(root: Option<Rc<RefCell<TreeNode>>>, k: i32) -> i32 {
        let mut array = Vec::<i32>::new();
        Solution::inorder(&root, &mut array);
        array[k as usize - 1]
    }

    fn inorder(node: &Option<Rc<RefCell<TreeNode>>>, arr: &mut Vec<i32>) {
        match node {
            Some(n) => {
                Solution::inorder(&n.borrow().left, arr);
                arr.push(n.borrow().val);
                Solution::inorder(&n.borrow().right, arr);
            }
            None => (),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let root = self::convert_to_tree_bfs(&vec![Some(3), Some(1), Some(4), None, Some(2)], 0);
        let k = 1;
        let expected = 1;
        let actual = Solution::kth_smallest(root, k);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = self::convert_to_tree_bfs(
            &vec![
                Some(5),
                Some(3),
                Some(6),
                Some(2),
                Some(4),
                None,
                None,
                Some(1),
            ],
            0,
        );
        let k = 3;
        let expected = 3;
        let actual = Solution::kth_smallest(root, k);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let root = self::convert_to_tree_bfs(&vec![Some(3), Some(1), Some(4), None, Some(2)], 0);
        let k = 1;
        let expected = 1;
        let actual = Solution::kth_smallest_nonrecur(root, k);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let root = self::convert_to_tree_bfs(
            &vec![
                Some(5),
                Some(3),
                Some(6),
                Some(2),
                Some(4),
                None,
                None,
                Some(1),
            ],
            0,
        );
        let k = 3;
        let expected = 3;
        let actual = Solution::kth_smallest_nonrecur(root, k);

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
