use std::cell::RefCell;
use std::rc::Rc;

use super::models::binary_tree_node::TreeNode;

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
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn case_recur_1() {
        let root = deserialize_to_BT(vec![Some(2), Some(1), Some(3)]);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_2() {
        let root = deserialize_to_BT(vec![
            Some(5),
            Some(1),
            Some(4),
            None,
            None,
            Some(3),
            Some(6),
        ]);
        let expected = false;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_3() {
        let root = deserialize_to_BT(vec![Some(i32::MAX)]);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_4() {
        let root = deserialize_to_BT(vec![Some(i32::MIN)]);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_5() {
        let root = deserialize_to_BT(vec![Some(i32::MAX), Some(i32::MAX)]);
        let expected = false;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_recur_6() {
        let root = deserialize_to_BT(vec![Some(0)]);
        let expected = true;
        let actual = Solution::is_valid_bst(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_1() {
        let root = deserialize_to_BT(vec![Some(2), Some(1), Some(3)]);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_2() {
        let root = deserialize_to_BT(vec![
            Some(5),
            Some(1),
            Some(4),
            None,
            None,
            Some(3),
            Some(6),
        ]);
        let expected = false;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_3() {
        let root = deserialize_to_BT(vec![Some(i32::MAX)]);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_4() {
        let root = deserialize_to_BT(vec![Some(i32::MIN)]);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_5() {
        let root = deserialize_to_BT(vec![Some(i32::MAX), Some(i32::MAX)]);
        let expected = false;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_6() {
        let root = deserialize_to_BT(vec![Some(0)]);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_nonrecur_7() {
        let root = deserialize_to_BT(vec![Some(0)]);
        let expected = true;
        let actual = Solution::is_valid_bst_nonrecur(root);

        assert_eq!(expected, actual);
    }
}
